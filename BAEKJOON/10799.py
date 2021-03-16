import sys
read=sys.stdin.readline

def VPS(str):
    global cut
    s_p=0
    stack=list()
    before=''
    while s_p<len(str):
        if str[s_p]=='(':
            stack.append('(')
            before='('
        elif str[s_p]==')':
            if stack:
                stack.pop(-1)
                if before=='(':
                    cut+=len(stack)
                else:
                    cut+=1       
                before=')'
            else:
                return 0
        s_p+=1
    
    if stack:
        return 0
    else:
        return 1

N=1
for _ in range(N):
    temp=read().strip()
    cut=0
    if VPS(temp):
        print(cut)
    else:
        print('NO')