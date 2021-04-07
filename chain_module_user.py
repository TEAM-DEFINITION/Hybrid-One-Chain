import hashlib
import endecrypt
import ast

'''

[db_user]
FileName : {{user_id}}_db

[variable]
USER_ID:str
USER_PASSWORD:str
DATA:str
PREV_HASH:str

'''

class user :
    def __init__(self):
        pass
    
    def genesis_block_create(self, user_id):
        
        genesis_block = ["USER_ID",
                    "USER_PASSWORD",
                    "DATA"
        ]

        f = open("db_user\\" + user_id + "_db","w")
        data = ""
        for i in genesis_block:
            data = data + i + "|"
        # print("제네시스블럭 : " + data)
        genesis_block.append(hashlib.sha512(data.encode('utf-8')).hexdigest())

        f.write("\n" + str(genesis_block))
        f.close()


        return 0


    def next_block_create(self, user_id, user_pwd, data):
        
        hardcoding = [user_id,
                    user_pwd,
                    data
        ]



        f = open("db_user\\" + user_id + "_db","r")
        prev_block = f.readlines()
        f.close()

        # 이전이전 데이터 Formating
        prev_data = ast.literal_eval(prev_block[-1])
        datas = ""
        for i in prev_data:
            datas = datas + str(i) + "|"
        # print("사용자가 보낸 블럭의 이전 데이터 : "+data)
        hardcoding.append(hashlib.sha512(datas.encode('utf-8')).hexdigest())

        # Test
        endecrypt.FerCipher(prev_block[-1]).decrypt(data)



        f = open("db_user\\" + user_id + "_db","a")
        f.write("\n" + str(hardcoding))
        f.close()

        # 서버 블록 생성
        server_block = [
            "K-Shield Jr. DEFINITION TEAM",
            "StoreAccess"
        ]
    
        f = open("db_user\\" + user_id + "_db","r")
        prev_block = f.readlines()
        f.close()

        # 이전 데이터 Formating
        prev_data = ast.literal_eval(prev_block[-1])
        data = ""
        for i in prev_data:
            data = data + i + "|"
        # print("서버가 만들 블럭의 이전 데이터 : "+data)

        server_block.append(hashlib.sha512(data.encode('utf-8')).hexdigest())
        f = open("db_user\\" + user_id + "_db","a")
        f.write("\n" + str(server_block))
        f.close()

        # 다시 최종 블럭의 데이터 가져오기
        f = open("db_user\\" + user_id + "_db","r")
        prev_block = f.readlines()
        f.close()

        # 데이터 암호화
        result = endecrypt.FerCipher(prev_block[-2]).encrypt(str(server_block))
        # result = endecrypt.encrypt(server_block, prev_block[-1])
        
        return result

    def check(self, user_id):

        # id만 체크함(수정필요)
        try:
            f = open("db_user\\" + user_id + "_db","r")
            prev_block = f.readlines()
            f.close()
        except:
            return 0
        return 0