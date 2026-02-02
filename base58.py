# Minimal base58 and placeholder classes for Piper
# For real use, replace with a vetted implementation!
import hashlib

__b58chars = '123456789ABCDEFGHJKLMNPQRSTUVWXYZabcdefghijkmnopqrstuvwxyz'
__b58base = len(__b58chars)

def b58encode(v):
    long_value = 0
    for (i, c) in enumerate(v[::-1]):
        long_value += (256**i) * c if isinstance(c, int) else ord(c)
    result = ''
    while long_value >= __b58base:
        div, mod = divmod(long_value, __b58base)
        result = __b58chars[mod] + result
        long_value = div
    result = __b58chars[long_value] + result
    nPad = 0
    for c in v:
        if c == 0:
            nPad += 1
        else:
            break
    return (__b58chars[0] * nPad) + result

def b58decode(v):
    long_value = 0
    for (i, c) in enumerate(v[::-1]):
        long_value += __b58chars.find(c) * (__b58base**i)
    result = b''
    while long_value >= 256:
        div, mod = divmod(long_value, 256)
        result = bytes([mod]) + result
        long_value = div
    result = bytes([long_value]) + result
    nPad = 0
    for c in v:
        if c == __b58chars[0]:
            nPad += 1
        else:
            break
    result = b'\x00' * nPad + result
    return result

def b58encode_check(v):
    h = hashlib.sha256(hashlib.sha256(v).digest()).digest()
    return b58encode(v + h[:4])

def b58decode_check(v):
    decoded = b58decode(v)
    data, cksum = decoded[:-4], decoded[-4:]
    vh = hashlib.sha256(hashlib.sha256(data).digest()).digest()[:4]
    if cksum != vh:
        raise ValueError('Invalid checksum')
    return data

class CBase58Data:
    def __init__(self, data, version):
        self.data = data
        self.version = version
    def __str__(self):
        return b58encode_check(bytes([self.version]) + self.data)

class CBitcoinAddress(CBase58Data):
    pass
