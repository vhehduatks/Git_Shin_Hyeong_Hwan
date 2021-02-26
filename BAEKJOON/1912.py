import sys 
read=sys.stdin.readline

def Bottom_up(N):
    dp[0]=A[0]
    for i in range(1,N):
        dp[i]=A[i]+max(dp[i-1],0)

    return max(dp)

N=int(read())
A=list(map(int,read().split()))
dp=[-1001]*(N+1)
print(Bottom_up(N))
