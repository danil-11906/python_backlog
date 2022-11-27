from Crypto.Hash import SHA256
from Crypto.PublicKey import RSA
from Crypto.Signature import pkcs1_15

import json


def parse_json(obj):
    return json.dumps(obj, sort_keys=True, indent=2)


def generate_keys():
    keySize = 2048

    key = RSA.generate(keySize)

    private_key = key.export_key('PEM', pkcs=8).decode('utf-8')
    public_key = key.publickey().export_key().decode('utf-8')

    file = open('public_key.pem', 'w')
    file.write(public_key)
    file.close()
    file = open('private_key.pem', 'w')
    file.write(private_key)
    file.close()


def read_key(filename):
    f = open(filename, mode='r')
    return RSA.importKey(f.read())


def get_private_key():
    return read_key('private_key.pem')


def get_public_key():
    return read_key('public_key.pem')


def transform_json_solve(solution, public_key):
    loss, weights = solution
    public_key_bytes = public_key.export_key()

    def get_float(num):
        return str(round(num, 12))

    return json.dumps({
        'w11': get_float(weights[0][0][0]),
        'w12': get_float(weights[0][0][1]),
        'w21': get_float(weights[0][1][0]),
        'w22': get_float(weights[0][1][1]),
        'v11': get_float(weights[1][0][0]),
        'v12': get_float(weights[1][0][1]),
        'v13': get_float(weights[1][0][2]),
        'v21': get_float(weights[1][1][0]),
        'v22': get_float(weights[1][1][1]),
        'v23': get_float(weights[1][1][2]),
        'w1': get_float(weights[2][0][0]),
        'w2': get_float(weights[2][1][0]),
        'w3': get_float(weights[2][2][0]),
        'e': get_float(loss),
        'publickey': public_key_bytes.hex(),
    })


def get_hash(info):
    return SHA256.new(info).digest()


def get_hash_for_sign(data, prev_hash):
    data_hash = get_hash(bytes(data, 'utf-8'))
    block_hash = get_hash(bytes(data, 'utf-8') + prev_hash)
    return block_hash + data_hash


def get_hash_for_arbiter(data, prev_hash, sign):
    return get_hash(prev_hash + bytes(data, 'utf-8') + sign)


def get_sign(data, prev_hash, private_key):
    h = SHA256.new(get_hash_for_sign(data, prev_hash))
    return pkcs1_15.new(private_key).sign(h)


def verify_sign(message, sign, public_key):
    h = SHA256.new(message)
    pkcs1_15.new(public_key).verify(h, sign)
