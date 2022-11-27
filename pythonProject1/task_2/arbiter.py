import json

import requests
from Crypto.Hash import SHA256
from Crypto.PublicKey import RSA
from Crypto.Signature import pkcs1_15

from task_2.block import Block
from task_2.utils import get_private_key, get_public_key

ARBITER_HOST = 'http://89.108.115.118'


class Arbiter:
    def __init__(self):
        resp = requests.get('%s/ts/public' % ARBITER_HOST)
        self.__public_key = RSA.importKey(bytes.fromhex(resp.text))
        self.__private_key = get_private_key()

    def get_public_key(self):
        return self.__public_key

    @staticmethod
    def get_token(block_hash):
        resp = requests.get('%s/ts?digest=%s' % (ARBITER_HOST, block_hash.hex()))
        content = resp.json()
        token = content['timeStampToken']
        time = token['ts']
        arb_sign = bytes.fromhex(token['signature'])

        return time, arb_sign

    @staticmethod
    def post_block(block):
        data = json.loads(block.data)
        resp_data = json.dumps({
            'prevhash': block.prev_hash.hex(),
            'data': data,
            'signature': block.sign.hex(),
        }).replace("'", '"').replace(' ', '')
        resp = requests.post('%s/nbc/newblock' % ARBITER_HOST, resp_data, headers={
            'Content-Type': 'application/json;charset=UTF-8'
        })

        print('Статус: %s' % resp.json()['status'])
        print(resp.json()['statusString'])

    def post_author(self):
        author = 'Дубровец Виталий Олегович, 11-902'
        h = SHA256.new(author.encode('utf-8'))
        sign = pkcs1_15.new(self.__private_key).sign(h)
        resp_data = json.dumps({
            'autor': author,
            'publickey': get_public_key().exportKey().hex(),
            'sign': sign.hex(),
        })
        resp = requests.post('%s/nbc/autor' % ARBITER_HOST, resp_data, headers={
            'Content-Type': 'application/json;charset=UTF-8'
        })
        print(resp_data)
        print(resp.json())
        print('Статус: %s' % resp.json()['status'])

    @staticmethod
    def __transform_json_to_block(json_block):
        prevhash = None
        if json_block['prevhash'] is not None:
            prevhash = bytes.fromhex(json_block['prevhash'])
        return Block(
            data=json.dumps(json_block['data'], separators=(',', ':')).replace("'", '"'),
            time=json_block['ts'],
            prev_hash=prevhash,
            sign=bytes.fromhex(json_block['signature']),
            arb_sign=bytes.fromhex(json_block['arbitersignature'])
        )

    def get_blockchain(self):
        resp = requests.get('%s/nbc/chain' % ARBITER_HOST)
        json_blocks = json.loads(resp.text)
        blocks = []
        for json_block in json_blocks:
            blocks.append(self.__transform_json_to_block(json_block))

        return blocks
