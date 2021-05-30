import os
import fnmatch
import random
# import asyncio


def check(postcode):

    # 가맹점 파일이 없으면 NULL값 리턴
    if os.path.isfile("db_store\\" + postcode + "_db") is False:
        return "NULL"

    # 가맹점 파일을 열어서 파일에 있는 정보 가져오기
    f = open("db_store\\" + postcode + "_db", "r", encoding="UTF8")
    post_block = f.readlines()
    f.close()

    # count에 따라 파일 정보 변경
    # count==1 이면 가맹점의 postcode를 변경하고 파일이름도 postcode에 따라 변경되고 count를 3으로 바꿈
    if post_block[2].split("|")[1] <= '1':
        post_block[2] = "Count|3|\n"

        while(True):
            a = 0
            newpostcode = random.randint(0, 99999)
            newpostcode = format(newpostcode, '05')

            for file_name in os.listdir("db_store"):
                if fnmatch.fnmatch(file_name, newpostcode + "_db"):
                    a = 1
            if(a == 0):
                break

        post_block[0] = "Number|" + str(newpostcode) + "|\n"

        f = open("db_store\\" + str(newpostcode) + "_db", "w", encoding="UTF8")
        f.write(''.join(post_block))
        f.close()
        os.remove("db_store\\" + str(postcode) + "_db")

    # count!=1 이면 count에서 -1을 빼줌
    else:
        count = int(post_block[2].split("|")[1])-1
        post_block[2] = "Count|"+str(count)+"|\n"

        f = open("db_store\\" + post_block[0].split("|")[1] + "_db", "w", encoding="UTF8")
        f.write(''.join(post_block))
        f.close()

    # 장소 리턴
    return post_block[1].split("|")[1]
