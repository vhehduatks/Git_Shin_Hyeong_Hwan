import sys
read=sys.stdin.readline


def recur(size):
    global cache
    
    if size==0:
        return 1

    if cache[size]:
        return cache[size]
    
    ret=0

    for i in range(1,3):
        if size-i>=0:
            ret+=recur(size-i)
    
    cache[size]=ret
    return ret

case_num=int(read())
for _ in range(case_num):
    size=int(read())
    cache=[None]*(size+1)
    print(cache)
    print(recur(size)%1000000007)