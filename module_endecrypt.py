# import os, hashlib
# import ast
# import json
from cryptography.fernet import Fernet
import rsa
import base64
import module_postcode
import datetime

from module_recovery import LOGING


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
        try:
            plain_text = cipher_suite.decrypt(data.encode())
        except Exception:
            LOGING.cipher()
        return plain_text.decode('utf-8'), module_postcode.check(plain_text.decode('utf-8').split("|")[2]), str(datetime.datetime.now())


class RSA_Cipher:

    def __init__(self):
        pass

    def encrypt(self):
        privateKeyBytes = open('rsa\\private.pem', 'r', encoding='utf-8').read()
        privateKey = rsa.PrivateKey._load_pkcs1_pem(keyfile=privateKeyBytes)
        encrypted = rsa.encrypt('123'.encode('utf-8'), privateKey)
        print(base64.b64encode(encrypted).decode('utf-8'))

    # def decrypt(self, data):
        # privateKeyBytes = open('rsa\\private.pem', 'rb').read()
        # privateKey = rsa.PublicKey.load_pkcs1_openssl_pem(keyfile=privateKeyBytes)
