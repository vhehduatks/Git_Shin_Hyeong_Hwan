import sys
read=sys.stdin.readline

def Bottom_up(N):
    cache[1][1]=1

    for n in range(2,N+1):
        cache[n][0]=cache[n-1][0]+cache[n-1][1]
        cache[n][1]=cache[n-1][0]
    
    ret=cache[N][0]+cache[N][1]
    return ret

test_case=int(read())
cache=[[0]*2 for _ in range(91)]
print(Bottom_up(test_case))