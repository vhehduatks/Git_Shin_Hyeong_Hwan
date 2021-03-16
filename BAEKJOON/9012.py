import sys
read=sys.stdin.readline

def VPS(str):
    s_p=0
    stack=list()

    while s_p<len(str):
        if str[s_p]=='(':
            stack.append('(')
        elif str[s_p]==')':
            if stack:
                stack.pop(-1)
            else:
                return 0
        s_p+=1
    
    if stack:
        return 0
    else:
        return 1

N=int(read())
for _ in range(N):
    temp=read().strip()
    if VPS(temp):
        print('YES')
    else:
        print('NO')