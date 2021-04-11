def check(postcode):
    
    print("사용자가 방문할 포스트 코드 : " + postcode)
    
    # 기존 가맹점 목록 불러오기
    f = open("db_store\\postcode","r", encoding="UTF8")
    prev_block = f.readlines()
    f.close()

    for i in prev_block:
        if i.find(postcode) == -1:
            pass
        else:
            return i.split("|")[1]
    return "00000"