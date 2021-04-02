import os, hashlib
from Cryptodome.Cipher import AES
import base64
import ast
import json

'''

Encryption Class : AES CBC MODE

'''

BS = 16
pad = lambda s: s + (BS - len(s.encode('utf-8')) % BS) * chr(BS - len(s.encode('utf-8')) % BS)
unpad = lambda s : s[:-ord(s[len(s)-1:])]
iv = b'\xa1R\xf7\xb9T\x1fS\xab\x168Q+\xc1\x91\xcea'

class AESCipher:
    def __init__( self, key ):
        self.key = key
        # 키 파싱
        self.key = ast.literal_eval(self.key)
        self.key = self.key[-1][:32].encode('utf-8')
        print(self.key)
        self.aes_key = []
        for parse in self.key:
            self.aes_key.append(hex(parse))

        '''
        
        self.temp = str(self.aes_key)
        self.temp = self.temp.replace("'","")
        self.temp = ast.literal_eval(self.temp)
        print(bytes(self.temp))

       self.aes_key_final = []
        self.aes_key_final = [ast.literal_eval(i) for i in self.aes_key]
        self.aes_key_final = bytes(self.aes_key_final)
        print(self.aes_key_final)
        

        '''


    def encrypt( self, raw ):
        print(raw)
        raw = pad(raw)
        cipher = AES.new( self.key, AES.MODE_CBC, iv )
        return base64.b64encode( iv + cipher.encrypt( raw.encode('utf-8') ) )

    def decrypt( self, enc ):
        enc = base64.b64decode(enc)
        iv = enc[:16]
        cipher = AES.new(self.key, AES.MODE_CBC, iv )
        return unpad(cipher.decrypt( enc[16:] ))



def gen_sha256_hashed_key_salt(key):
    salt = hashlib.sha512(key.encode()).digest()
    return hashlib.sha512(salt+key.encode()).digest()


def encrypt(server_block, key): 

    # 서버데이터를 Formating
    server_block = list(server_block)
    data = ""
    for i in server_block:
        data = data + i + "|"

    # 키 파싱
    key = ast.literal_eval(key)
    key = key[-1][:32].encode('utf-8')
    aes_key = []
    for parse in key:
        aes_key.append(hex(parse))

    # 암호화 준비
    Blocksize = 16
    pad = lambda s: s + (Blocksize - len(s.encode('utf-8')) % Blocksize) * chr(Blocksize - len(s.encode('utf-8')) % Blocksize)
    pad_data = pad(data)
    iv = b"2fad5a477d13ecda7f718fbd8a9f0443"
    cipher = AES.new(key, AES.MODE_CBC, iv[:16])

    # 복호화 테스트
    unpad = lambda s : s[:-ord(s[len(s)-1:])]
    encrypted_data = cipher.encrypt(pad_data.encode('utf-8'))
    print(encrypted_data)
    try :
        print(unpad(cipher.decrypt(encrypted_data).decode('utf-8')))
    except :
        print("???")

    return cipher.encrypt(pad_data.encode('utf-8'))




    '''key = gen_sha256_hashed_key_salt((key.split(",")[-1].replace("']", "")[2:]))
    iv = b"2fad5a477d13ecda7f718fbd8a9f0443"
    encryptor = AES.new(key[:16], AES.MODE_CBC, iv[:16])
    return encryptor.encrypt(pad_data.encode('utf-8'))'''


def decrypt(enc, key): 
    unpad = lambda s: s[:-ord(s[len(s) - 1:])]
    key = gen_sha256_hashed_key_salt((key.split(",")[-1].replace("']", "")[2:]))
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
