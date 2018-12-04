"""designed to use Pycrypto to decrypt AES
- Matthew Norloff
"""
from Crypto.Cipher import AES


key = b'\xbf\xc0\x85)\x10nc\x94\x02)j\xdf\xcb\xc4\x94\x9d(\x9e[EX\xc8\xd5\xbfI{\xa2$\x05(\xd5\x18'
cipher = AES.new(key)


def decrypt(ciphertext):
    global cipher
    dec = cipher.decrypt(ciphertext).decode('utf-8')
    l = dec.count('{')
    return dec[:len(dec)-l]
