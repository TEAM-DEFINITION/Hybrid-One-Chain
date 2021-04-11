import os, hashlib
from cryptography.fernet import Fernet
import base64
#import ast
import json

'''

Encrypt Mode : Fernet
Decrypt Mode : Fernet

Key size : 32bytes

'''
class FerCipher:

    def __init__(self, key):
        self.key = key
        # 키 파싱
        self.key = self.key[:32].encode('utf-8')
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
        return plain_text.decode('utf-8')

