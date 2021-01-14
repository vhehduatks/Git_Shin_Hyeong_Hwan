import sys
read=sys.stdin.readline

#입력처리
case_num=int(read())
S_F_num=list()
F_num=list()
for i in range(case_num*2):
    #학생수와 친구쌍의 수
    if i%2==0:
        S_F_num.append(list(map(int,read().strip().split())))
    elif i%2==1:
        F_num.append(list(map(int,read().strip().split())))

#S_Fnum의 col은 0=학생수 1=친구쌍의 수
#F_num은 2%1마다 서로 친구인 번호

def make_F_matrix(S_num,F_list):
    #파이썬에서 리스트를 따로 만들고 해당 리스트로 2차원 리스트를 만들면 파이썬의 얉은 복사 때문에 모든 리스트가 같은 리스트가 됨
    # col_list=[False for _ in range(S_num)]
    # f_matrix=[col_list for _ in range(S_num)] //<< 모든 행이 하나의 col_list가 된다. 하나의 열만 바꿔도 모든 행이 바껴버림;
    
    #학생수x학생수의 2차원 배열 생성 =서로 친구인지 확인하기 위해

    f_matrix=[[False for _ in range(S_num[0])] for _ in range(S_num[0])]

    for i in range(int(S_num[1]/2)):
        row=F_list[i*2]
        col=F_list[i*2+1]
        f_matrix[row][col]=True

    return f_matrix

def Pairing(has_pairing,S_num,f_matrix):
    fast_num=-1
    
    for i in range(len(has_pairing)):
        if not(has_pairing[i]):
            
            fast_num=i
            break
    print("hp:",has_pairing)
    print("Fn:",fast_num)
    

    if fast_num==-1:
        print("work?")    
        return 1

    ret=0
    for i in range(fast_num+1,S_num[0]):
        if (not(has_pairing[i]))and(f_matrix[fast_num][i]):
            has_pairing[fast_num]=True
            has_pairing[i]=True
            ret+=Pairing(has_pairing,S_num,f_matrix)
            has_pairing[fast_num]=False
            has_pairing[i]=False
    print("ret:",ret)
    return ret

def use_pairing(S_F_num,F_num,case_num):
    for i in range(case_num):
        temp_matrix=make_F_matrix(S_F_num[i],F_num[i])
        temp_has_pairing=[False for _ in range(S_F_num[i][0])]
        output=Pairing(temp_has_pairing,S_F_num[i],temp_matrix)
        print(output)

use_pairing(S_F_num,F_num,case_num)