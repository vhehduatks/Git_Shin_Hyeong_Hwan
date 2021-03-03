import sys
read=sys.stdin.readline

dp=[None]*101
def bottom_up(N):
    dp[1]=1
    dp[2]=1
    dp[3]=1
    dp[4]=2
    dp[5]=2

    if N>5:
        for n in range(6,N+1):
            dp[n]=dp[n-1]+dp[n-5]
    
    return dp[N]

case_num=int(read())

for _ in range(case_num):
    print(bottom_up(int(read())))