import sys
read=sys.stdin.readline

def recur(n):
    if n==0:
        return 1
    if cache[n]:
        return cache[n]
    ret=0
    for i in range(1,4):
        if n-i>=0:
            ret+=recur(n-i)
    cache[n]=ret
    return ret

case_num=int(read())
cache=[None]*12
for _ in range(case_num):
    print(recur(int(read())))