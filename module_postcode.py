import os
import fnmatch
import random
import asyncio

def check(postcode):
    
    # 가맹점 파일이 없으면 NULL값 리턴
    if os.path.isfile("db_store\\" + postcode + "_db") == False :
        return "NULL"

    # 파일을 열어서 파일에 있는 정보 가져오기
    f = open("db_store\\" + postcode + "_db","r", encoding="UTF8")
    post_block = f.readlines()
    f.close()

    # count
    if post_block[2].split("|")[1] == '1': # count가 1이면 count를 3으로 바꿈
        post_block[2] = "Count|3|\n"
        
        while(True) :
            a=0
            newpostcode = random.randint(0,99999)
            print(newpostcode)
            newpostcode = format(newpostcode, '05')
            for file_name in os.listdir("db_store"):
                if fnmatch.fnmatch(file_name, newpostcode +"_db"):
                  a=1
            if(a==0):
                break
        post_block[0]="Number|"+ str(newpostcode)+"|\n"
        f = open("db_store\\" + str(newpostcode) + "_db","w", encoding="UTF8")
        f.write(''.join(post_block))
        f.close()
        postcode=newpostcode

        print(post_block)

    else: # count가 1이 아니면 -1을 함
        count = int(post_block[2].split("|")[1])-1
        post_block[2]="Count|"+str(count)+"|\n"
        print(post_block)
        # count-=1

    # count 수정 사항 파일에 쓰기
    f = open("db_store\\" + post_block[0].split("|")[1] + "_db","w", encoding="UTF8")
    f.write(''.join(post_block))
    f.close()

    # count가 0이면 counting()함수
    '''if post_block[2].split("|")[1] == 0:
        counting(post_block)
    else:
        pass
    '''

    # 장소를 리턴
    return post_block[1].split("|")[1]


  # 비동기 함수 만들기 count -> count를 3번으로 바꾸고 postcode도 바꾸고 파일명도 바꾸고
#async def counting(post_block):
    # postcode += 10
   #postcode = int(post_block[0].split("|")[1])
    #print("\n\n\na\n\n\n\n")
                
    #post_block[0].split("|")[1] = str(postcode) 

    # count = 3
    #post_block[2].split("|")[1] = '3'

    # 새로운 파일 만들기
    #f = open("db_store\\" + post_block[0].split("|")[1] + "_db","w", encoding="UTF8")
    #f.write(post_block)
    #f.close()
    
    #return post_block

'''
    # 증명장소 가져오기 -> HyperAccessServer
    for k in post_block:
        if k.find('Certification') == -1:
            pass
        else:
            return k.split("|")[1]
    return "NULL"'''