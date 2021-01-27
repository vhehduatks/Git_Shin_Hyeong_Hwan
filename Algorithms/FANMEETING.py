import sys
read=sys.stdin.readline

def hug(F_list,M_list):
    M_len=len(M_list)
    F_len=len(F_list)
    ret=0

    for i in range((F_len+1)-M_len):
        Allhug=True
        for j in range(M_len):
            # print(F_list[i+j],M_list[j])
            if F_list[i+j]*M_list[j]:
                # print("work")
                Allhug=False
                break
        if Allhug:
            ret+=1
    
    return ret

case_num=int(read())

for _ in range(case_num):
    M_list=list(map(lambda x:x=='M',list(read().strip())))
    F_list=list(map(lambda x:x=='M',list(read().strip())))
    print(hug(F_list,M_list))