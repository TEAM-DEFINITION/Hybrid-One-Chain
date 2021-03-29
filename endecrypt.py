import base64, os
import hmac, binascii
from Cryptodome.Cipher import AES


def encrypt(data, key): 
    data = '@@'.join(data)
    BS = 16
    pad = lambda s: s + (BS - len(s.encode('utf-8')) % BS) * chr(BS - len(s.encode('utf-8')) % BS)
    raw = pad(data)
    key = (key.split(",")[-1].replace("']", "")[2:]).encode()
    iv = b"2fad5a477d13ecda7f718fbd8a9f0443"
    encryptor = AES.new(key[:16], AES.MODE_CBC, iv[:16])
    return base64.b64encode(encryptor.encrypt(raw.encode('utf-8')))


def decrypt(enc, key): 
    enc = base64.b64decode(enc)
    unpad = lambda s: s[:-ord(s[len(s) - 1:])]
    key = (key.split(",")[-1].replace("']", "")[2:]).encode()
    iv = b"2fad5a477d13ecda7f718fbd8a9f0443"
    decryptor = AES.new(key[:16], AES.MODE_CBC, iv[:16])
    return str(unpad(decryptor.decrypt(enc)))[2:-1].split('@@')
    

'''
if __name__ == '__main__':

    key = b'6ab68bce1bb1a1fbb686cee02a29214552d0d2af2ca822570fed4937c66d107539338c76587e1321eca426e099791cdea82696cd46320d0790555d2cadd9491c'
    server_block = [
        "K-Shield Jr. DEFINITION TEAM",
        "2BD1144CFFE6D3A71A85B1ECFFE4D4EFA50EAD8186731E7FC8EE42FB4F814CE4C31E721FFE9F6DC9D4B2585F15F570045FC6A94EED99A1779E97C64142D3CF41",
        "Authentiacation Complete!!"
    ]
    print(encrypt(server_block, key))
    '''
''''
    server_block = [
        "K-Shield Jr. DEFINITION TEAM",
        "2BD1144CFFE6D3A71A85B1ECFFE4D4EFA50EAD8186731E7FC8EE42FB4F814CE4C31E721FFE9F6DC9D4B2585F15F570045FC6A94EED99A1779E97C64142D3CF41",
        "Authentiacation Complete!!"
    ]
'''
   