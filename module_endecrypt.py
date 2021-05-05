import os, hashlib
from cryptography.fernet import Fernet
import base64
#import ast
import json
import module_postcode
import datetime

from module_recovery import *


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
        self.key = base64.urlsafe_b64encode(self.key)

    def encrypt(self, data):
        cipher_suite = Fernet(self.key)
        cipher_text = cipher_suite.encrypt(data.encode())
        return cipher_text

    def decrypt(self, data):
        cipher_suite = Fernet(self.key)
        try :
            plain_text = cipher_suite.decrypt(data.encode())
        except :
            LOGING.cipher()
        return plain_text.decode('utf-8'), module_postcode.check(plain_text.decode('utf-8').split("|")[2]), str(datetime.datetime.now())

