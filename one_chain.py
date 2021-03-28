import hashlib
import time



def genesis_block_create():

    hardcoding = ["USER_ID",
                "USER_PASSWORD",
                "DATA"
    ]

    f = open("chain_db","w")

    new_hash = hash(hardcoding)
    hardcoding.append(new_hash)

    f.write(str(hardcoding) + "\n")
    f.close()


    return 0

def next_block_create(user_id, user_pwd):
    
    hardcoding = [user_id,
                user_pwd
    ]

    f = open("chain_db","r")
    prev_block = f.readlines()
    f.close()

    
    hardcoding.append(hashlib.sha512(str(prev_block[-1]).encode('utf-8')).hexdigest())
    f = open("chain_db","a")
    f.write(str(hardcoding) + "\n")
    f.close()

    # 서버 블록 생성
    server_block = [
        "SERVER_NAME",
        "SERVER_KEY"
    ]

    f = open("chain_db","r")
    prev_block = f.readlines()
    f.close()

    
    server_block.append(hashlib.sha512(str(prev_block[-1]).encode('utf-8')).hexdigest())
    f = open("chain_db","a")
    f.write(str(server_block) + "\n")
    f.close()

    return 0

def hash(block):
    result = hashlib.sha512(str(block).encode('utf-8')).hexdigest()
    return result