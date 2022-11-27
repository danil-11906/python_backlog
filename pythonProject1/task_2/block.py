import json


class Block:
    def __init__(self, data, prev_hash, sign, time, arb_sign):
        self.data = data
        self.prev_hash = prev_hash
        self.time = time
        self.sign = sign
        self.arb_sign = arb_sign

    def __str__(self):
        data = json.loads(self.data)
        return 'data: %s\nprev_hash: %s\nsign: %s\ntime: %s\narg_sign: %s' % (data, self.prev_hash, self.sign, self.time, self.arb_sign)