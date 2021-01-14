import sys
read=sys.stdin.readline


def DFS(has_pair,is_friend):
    no_pair=-1
    for i in range(len(has_pair)):
        if not(has_pair[i]):
            no_pair=i
            break
    if no_pair==-1:
        return 1
    
    total=0

    for i in range(no_pair+1,n):
        if not(has_pair[i])and(is_friend[no_pair][i]):
            has_pair[i]=True
            has_pair[no_pair]=True
            total+=DFS(has_pair,is_friend)
            has_pair[i]=False
            has_pair[no_pair]=False
    
    return total
#https://hellominchan.tistory.com/248 참고

#입력처리
case_num=int(read())

for _ in range(case_num):
    n,m=map(int,read().split())
    f=list(map(int,read().split()))
    has_pair=[False]*n
    is_friend=[[False]*n for _ in range(n)]

    for i in range(0,len(f),2):
        row=f[i]
        col=f[i+1]
        is_friend[row][col]=True
        is_friend[col][row]=True
    
    print(DFS(has_pair,is_friend))



