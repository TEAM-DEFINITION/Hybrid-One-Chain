import os, hashlib
from Cryptodome.Cipher import AES
from cryptography.fernet import Fernet
import base64
import ast
import json

'''

Encryption Class : AES CBC MODE

'''

BS = 16
pad = lambda s: s + (BS - len(s.encode('utf-8')) % BS) * chr(BS - len(s.encode('utf-8')) % BS)
unpad = lambda s : s[:-ord(s[len(s)-1:])]
iv = "0000000000000000".encode('utf-8')

class AESCipher:
    def __init__( self, key ):
        self.key = key
        # 키 파싱
        self.key = ast.literal_eval(self.key)
        # print(self.key[-1][:32])
        self.key = self.key[-1][:32].encode('utf-8')
        # print(self.key)
        self.aes_key = []
        for parse in self.key:
            self.aes_key.append(hex(parse))

    def encrypt( self, raw ):
        # 데이터 Formating
        prev_data = ast.literal_eval(raw)
        data = ""
        for i in prev_data:
            data = data + i + "|"
        # print("보낼 데이터 : "+data)
        # print("이니셜백터 : " + str(iv))
        raw = pad(data)
        cipher = AES.new( self.key, AES.MODE_CBC, iv )
        return base64.b64encode(cipher.encrypt( raw.encode('utf-8') ) )

    def decrypt( self, enc ):
        print("복호화 키 : " + str(self.key))
        enc = base64.b64decode(enc)
        print("사용자로부터 받은 데이터  => " + str(enc))
        iv = enc[:16]
        cipher = AES.new(self.key, AES.MODE_CBC, iv )
        print("복호화한 데이터 : " + str(cipher.decrypt( enc[16:] )))
        # return unpad(cipher.decrypt( enc[16:] ))

class FerCipher:
    # key = 32 bytes

    def __init__(self, key):
        self.key = key
        # 키 파싱
        self.key = ast.literal_eval(self.key)
        self.key = self.key[-1][:32].encode('utf-8')
        print("키변환" + str(self.key))
        self.key = base64.urlsafe_b64encode(self.key)
        print("키변환끝" + str(self.key))

    def encrypt(self, data):
        print("암호화 키값 : " + str(self.key))
        print("암호화할 데이터 : " + data)
        cipher_suite = Fernet(self.key)
        cipher_text = cipher_suite.encrypt(data.encode())
        print("보낼 암호문 : " + cipher_text.decode('utf-8'))
        return cipher_text

    def decrypt(self, data):
        print("복호화 키값 : " + str(self.key))
        print("복호화할 데이터 : " + str(data.encode()))
        cipher_suite = Fernet(self.key)
        plain_text = cipher_suite.decrypt(data.encode())
        print("유저로부터 받은 데이터 : " + str(plain_text))
        return 0

