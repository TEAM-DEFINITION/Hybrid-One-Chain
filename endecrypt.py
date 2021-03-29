import base64, os
import hmac, binascii
from Cryptodome import Random
from Cryptodome.Cipher import AES


def encrypt(data, key):  # 박성현 파트
    BS = 16
    pad = lambda s: s + (BS - len(s.encode('utf-8')) % BS) * chr(BS - len(s.encode('utf-8')) % BS)
    raw = pad(data)
    iv = os.urandom(16)
    encryptor = AES.new(key[:16], AES.MODE_CBC, iv)
    return base64.b64encode( iv + encryptor.encrypt( raw.encode('utf-8') ) )

def decrypt(enc, key):  # 박성현 파트
    enc = base64.b64decode(enc)
    unpad = lambda s: s[:-ord(s[len(s) - 1:])]
    iv = enc[:16]
    decryptor = AES.new(key[:16], AES.MODE_CBC, iv)
    return unpad(decryptor.decrypt(enc[16:]))

if __name__ == '__main__':
    data = str(input())
    key = b'6ab68bce1bb1a1fbb686cee02a29214552d0d2af2ca822570fed4937c66d107539338c76587e1321eca426e099791cdea82696cd46320d0790555d2cadd9491c'

    print(encrypt(data, key))
    print(decrypt(encrypt(data, key), key))

''''
def gen_AES128_hashed_key_salt(key):
    salt1 = hmac.new(key).digest()
    return salt1


def encrypt(data, key):  # 박성현 파트
    iv = os.urandom(16)
    encryptor = AES.new(key ,AES.MODE_CBC, iv)
    return encryptor.encrypt(data)

def decrypt(data, key):  # 최진호 파

    def AES128Decrypt(data, key):
    encryptor = AES.new(key, AES.MODE_CBC)
    # plain = encrypt.decrypt()

    return result
   

if __name__ == '__main__':
    data = str(input())
    key = '6ab68bce1bb1a1fbb686cee02a29214552d0d2af2ca822570fed4937c66d107539338c76587e1321eca426e099791cdea82696cd46320d0790555d2cadd9491c'

    '''
# key = '' 
# def AES128Decrypt(key.iv,cipher)
# encr

'''
성현 : 
현성 : ㅋㅋㄹㅃㅃ
진호 : self랑 data 바꿔줘야대는거아녜여ㅑ?

'''
   