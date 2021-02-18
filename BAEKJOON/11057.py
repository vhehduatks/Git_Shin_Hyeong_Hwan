import sys
read=sys.stdin.readline

def top_down(n,k):
    if n==0:
        return 1

    if cache[n][k]:
        return cache[n][k]
    
    ret=0

    for i in range(k,10):
        ret+=top_down(n-1,i)
    
    cache[n][k]=ret
    # print(cache)
    return ret


test_case=int(read())
cache=[[None]*10 for _ in range(1001)]
print(top_down(test_case,0)%10007)
