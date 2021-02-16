import sys
read=sys.stdin.readline
sys.setrecursionlimit(10**7)

def tailing(size):
    if size==0:
        return 1

    if cache[size]:
        return cache[size]
    
    ret=0

    for i in range(1,3):
        if size-i>=0:
            ret+=i*tailing(size-i)
    cache[size]=ret

    return ret

test_case=int(read())
cache=[None]*(1001)
print(tailing(test_case)%10007)