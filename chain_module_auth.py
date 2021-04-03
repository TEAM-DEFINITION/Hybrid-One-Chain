import hashlib
import endecrypt
import ast

'''

[Authchain Format]
USER_ID:str
USER_PASSWORD:str
DATA:str

'''

def genesis_block_create(user_id):
    
    hardcoding = ["USER_ID",
                "USER_PASSWORD",
                "DATA"
    ]

    f = open("db_user\\" + user_id + "_db","w")

    new_hash = hash(hardcoding)
    hardcoding.append(new_hash)

    f.write("\n" + str(hardcoding))
    f.close()


    return 0

#########################################################################################

def next_block_create(user_id, user_pwd, data):
    
    hardcoding = [user_id,
                user_pwd,
                data
    ]

    # 회원가입된 체인인지 확인
    try:
        f = open("db_user\\" + user_id + "_db","r")
        prev_block = f.readlines()
        f.close()
    except:
        return 0

    # 이전이전 데이터 Formating
    prev_data = ast.literal_eval(prev_block[-1])
    data = ""
    for i in prev_data:
        data = data + i + "|"
    print("사용자가 보낸 블럭의 이전 데이터 : "+data)
    hardcoding.append(hashlib.sha512(data.encode('utf-8')).hexdigest())



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
    print("서버가 만들 블럭의 이전 데이터 : "+data)

    server_block.append(hashlib.sha512(data.encode('utf-8')).hexdigest())
    f = open("db_user\\" + user_id + "_db","a")
    f.write("\n" + str(server_block))
    f.close()

    # 다시 최종 블럭의 데이터 가져오기
    f = open("db_user\\" + user_id + "_db","r")
    prev_block = f.readlines()
    f.close()

    try :
        # 데이터 암호화
        result = endecrypt.AESCipher(prev_block[-1]).encrypt(str(server_block))
        # result = endecrypt.encrypt(server_block, prev_block[-1])
    except : 
        # 실패시 오류 반환
        result = "서버에서 데이터암호화에 실패하였습니다!"
    
    return result

def hash(block):
    result = hashlib.sha512(str(block).encode('utf-8')).hexdigest()
    return result

def check(user_id):

    # id만 체크함(수정필요)
    try:
        f = open("db_user\\" + user_id + "_db","r")
        prev_block = f.readlines()
        f.close()
    except:
        return 0
    return 0