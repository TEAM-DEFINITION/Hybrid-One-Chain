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
        self.aes_key = []
        for parse in self.key:
            self.aes_key.append(hex(parse))

    def encrypt( self, raw ):
        # 이전 데이터 Formating
        prev_data = ast.literal_eval(raw)
        data = ""
        for i in prev_data:
            data = data + i + "|"
        print("보낼 데이터 : "+data)

        raw = pad(data)
        cipher = AES.new( self.key, AES.MODE_CBC, iv )
        return base64.b64encode( iv + cipher.encrypt( raw.encode('utf-8') ) )

    def decrypt( self, enc ):
        enc = base64.b64decode(enc)
        iv = enc[:16]
        cipher = AES.new(self.key, AES.MODE_CBC, iv )
        return unpad(cipher.decrypt( enc[16:] ))
