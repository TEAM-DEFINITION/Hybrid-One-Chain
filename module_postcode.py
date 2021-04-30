def check(postcode):
    
    # 기존 가맹점 목록 불러오기
    f = open("db_store\\postcode","r", encoding="UTF8")
    prevBlock = f.readlines()
    f.close()

    # 포스트코드 찾기
    for i in prevBlock:
        if i.find(postcode) == -1:
            pass
        else:
            return i.split("|")[1]
    return "NULL"