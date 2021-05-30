import hashlib
import module_endecrypt
# import ast 
# import time
import os

class USER:
    def __init__(self):
        pass

    def login(self, user_id, user_pwd):

        # 아이디 확인
        if os.path.isfile("./db_user/" + user_id + "_db") == False:
            return 401


        f = open("db_user\\" + user_id + "_db", "r", encoding="UTF8")
        temp = f.readlines()
        f.close()

        # 비밀번호 확인
        if temp[1].split("|")[1] == hashlib.sha512(user_pwd.encode('utf-8')).hexdigest():
            return 200
        else:
            return 402
    
    def genesis_block_create(self, user_id, user_pwd, clientrandom):

        # 아이디 중복 확인
        if os.path.isfile("./db_user/" + user_id + "_db"):
            return 401
        
        hashedPassword = hashlib.sha512(user_pwd.encode('utf-8')).hexdigest()

        genesis_block = user_id + "|" + hashedPassword + "|" + clientrandom +"|"
        genesis_block = genesis_block + hashlib.sha512(genesis_block.encode('utf-8')).hexdigest() +"|"

        f = open("db_user\\" + user_id + "_db", "w", encoding="UTF8")
        f.write("\n" + genesis_block)
        f.close()

        return 200


    def next_block_create(self, user_id, user_pwd, data):

        # 이전 블록 읽어오기
        f = open("db_user\\" + user_id + "_db", "r", encoding="UTF8")

        prev_block = f.readlines()
        f.close()

        # 이전 블록의 해시값을 사용자 블록에 쓰기
        prev_data = prev_block[-1]
        result, place, time = module_endecrypt.FerCipher(prev_data.split("|")[3]).decrypt(data)

        new_block = result + hashlib.sha512(prev_data.encode('utf-8')).hexdigest() + "|"
        f = open("db_user\\" + user_id + "_db", "a", encoding="UTF8")
        f.write("\n" + new_block)
        f.close()

        # 서버 블록 포맷
        server_block = "HybridAccessServer|" + place + "|" + time + "|"

        # 새로운 블록을 쓰기 위해 수정된 체인 읽기
        f = open("db_user\\" + user_id + "_db", "r", encoding="UTF8")
        prev_block = f.readlines()
        f.close()

        # 사용자 블록의 해시값을 추출하여 추가
        prev_data = prev_block[-1]
        server_block = server_block + hashlib.sha512(prev_data.encode('utf-8')).hexdigest() + "|"
        f = open("db_user\\" + user_id + "_db", "a", encoding="UTF8")
        f.write("\n" + server_block)
        f.close()

        # 최종 체인의 정보를 읽어옴
        f = open("db_user\\" + user_id + "_db", "r", encoding="UTF8")
        prev_block = f.readlines()
        f.close()

        # 보낼 데이터를 n-1번째 체인의 해시값으로 암호화
        result = module_endecrypt.FerCipher(prev_block[-2].split("|")[3]).encrypt(server_block)
        return result
