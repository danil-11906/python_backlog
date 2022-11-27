import psycopg2

from task_2 import settings
from task_2.block import Block
from task_2.utils import parse_json


class SQLWorker:
    def __init__(self):
        conn = psycopg2.connect(dbname=settings.DATABASE, user=settings.LOGIN,
                                password=settings.PASSWORD, host=settings.HOST)
        self.__conn = conn
        self.__cursor = conn.cursor()

    @staticmethod
    def __map_item_to_block(item):
        return Block(data=parse_json(item[0]), sign=bytes(item[1]), prev_hash=item[2], time=item[3], arb_sign=bytes(item[4]))

    def add_block(self, block):
        self.__cursor.execute("insert into blockchain (data, sign, prev_hash, time, arb_sign) VALUES (%s, %s, %s, %s, %s)", (block.data, block.sign, block.prev_hash, block.time, block.arb_sign))
        self.__conn.commit()

    def get_blocks(self):
        self.__cursor.execute("select data, sign, prev_hash, time, arb_sign from blockchain")
        items = self.__cursor.fetchall()
        return list(map(self.__map_item_to_block, items))

    def update_block(self, block, prev_hash):
        self.__cursor.execute("update blockchain SET (data, sign, prev_hash, time, arb_sign) = (%s, %s, %s, %s, %s) where prev_hash = (%s)", (block.data, block.sign, block.prev_hash, block.time, block.arb_sign, prev_hash))
        self.__conn.commit()

    def get_block_by_prev_hash(self, prev_hash):
        self.__cursor.execute("select data, sign, prev_hash, time, arb_sign from blockchain where prev_hash = (%s)", (prev_hash,))
        item = self.__cursor.fetchone()
        return item if item is None else self.__map_item_to_block(item)
