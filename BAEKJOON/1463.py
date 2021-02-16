import sys
read=sys.stdin.readline
INF=float('inf')
def bottom_up(n):
    cache[1]=0
    for i in range(2,n+1):
        if i%2==0:
            cache[i]=min(cache[i],cache[int(i/2)]+1)
        if i%3==0:
            cache[i]=min(cache[i],cache[int(i/3)]+1)
        cache[i]=min(cache[i],cache[i-1]+1)

    return cache[n]

cache=[INF]*(1000000+1)
print(bottom_up(int(read())))