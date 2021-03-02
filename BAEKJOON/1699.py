import math
import sys
read=sys.stdin.readline
N=int(read())
INF=float('inf')
dp=[None]*(100001)
def bottom_up(n):
    dp[0]=0

    for i in range(1,N+1):
        x=int(math.sqrt(i))
        dp[i]=INF
        for j in range(1,x+1):
            dp[i]=min(dp[i],dp[i-j**2]+1)
            
    return dp[n]

print(bottom_up(N))