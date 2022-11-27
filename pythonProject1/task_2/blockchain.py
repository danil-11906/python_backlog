import json
from datetime import datetime

import numpy as np

from task_2.arbiter import Arbiter
from task_2.block import Block
from task_2.neuronet import NeuroNetwork
from task_2.sql import SQLWorker
from task_2.utils import get_private_key, get_public_key, get_hash, get_hash_for_sign, parse_json, get_hash_for_arbiter, \
    transform_json_solve, get_sign, verify_sign


class BlockchainManager:
    def __init__(self):
        self.__arbiter = Arbiter()
        self.__private_key = get_private_key()
        self.__public_key = get_public_key()
        self.__sql_worker = SQLWorker()
        self.__blockchain = []

    def add_block(self, data, blocks, to_db=True):
        prev_hash = bytes()
        if len(blocks) > 0:
            last_block = blocks[-1]
            last_prev_hash = bytes()
            if last_block.prev_hash is not None:
                last_prev_hash = last_block.prev_hash
            items = [last_prev_hash, bytes(data, 'utf-8'), last_block.sign]
            prev_hash = get_hash(items[0] + items[1] + items[2])
        sign = get_sign(data=data, prev_hash=prev_hash, private_key=self.__private_key)
        (time, arb_sign) = self.__arbiter.get_token(get_hash_for_arbiter(data, prev_hash, sign))
        block = Block(data=data, prev_hash=prev_hash, sign=sign, time=time, arb_sign=arb_sign)
        blocks.append(block)
        if to_db:
            self.__sql_worker.add_block(block)
        return block

    def get_blockchain_from_db(self):
        self.__blockchain = self.__sql_worker.get_blocks()
        return self.__blockchain

    def get_blockchain_from_arbiter(self):
        self.__blockchain = self.__arbiter.get_blockchain()
        return self.__blockchain

    def generate_blockchain(self):
        for i in range(0, 100):
            data = parse_json({
                'timestamp': str(datetime.now()),
                'items': list(np.random.rand(1, 5)[0])
            })
            self.add_block(data, self.__blockchain)
            return self.__blockchain

    def damage_random_block(self, blocks):
        index = np.random.randint(len(blocks))
        rand_block = blocks[index]
        json_data = json.loads(rand_block.data)
        rand_block.data = parse_json({
            'timestamp': json_data['timestamp'],
            'items': [666]
        })
        self.__sql_worker.update_block(rand_block, rand_block.prev_hash)

    def check_chain_validity(self, blocks):
        blockchain_len = len(blocks)
        prev_block = None
        block = blocks[0]
        is_valid = True
        for i in range(0, blockchain_len):
            if block is None:
                print("INVALID BLOCK DETECTED")
                print(prev_block)
                is_valid = False
                break
            else:
                is_valid = self.is_block_correct(block)
                if not is_valid:
                    print("INVALID SIGNED BLOCK DETECTED")
                    print(block)
                    break
                block_hash = get_hash(block.prev_hash + bytes(block.data, 'utf-8') + block.sign)
                block = self.__sql_worker.get_block_by_prev_hash(block_hash)
                prev_block = block

        if is_valid:
            print("Chain is valid")

    def is_block_correct(self, block):
        try:
            block_hash = get_hash_for_arbiter(block.data, block.prev_hash, block.sign)
            verify_sign(str(block.time).encode() + bytes(block_hash), block.arb_sign, self.__arbiter.get_public_key())
            verify_sign(get_hash_for_sign(data=block.data, prev_hash=block.prev_hash), block.sign, self.__public_key)
            return True
        except (ValueError, TypeError):
            return False

    def get_blockchain(self):
        return self.__blockchain

    def print_blockchain(self):
        print("Blockchain size: %d\n" % len(self.__blockchain))
        for block in self.__blockchain:
            print(block)
            print("-" * 30)

    def add_solution_block(self):
        neuro_network = NeuroNetwork()
        block_data = transform_json_solve(neuro_network.solve_task(), self.__public_key)
        return self.add_block(block_data, self.__blockchain, to_db=False)

    def get_arbiter(self):
        return self.__arbiter