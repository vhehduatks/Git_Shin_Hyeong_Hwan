import sys
read=sys.stdin.readline

def bottom_up(N):
   
    if N==1:
        return A[1]
    elif N==2:
        return A[1]+A[2]
    # elif N==3:
    #     return A[2]+max(A[0],A[1])

    dp[1]=A[1]
    dp[2]=A[1]+A[2]
  
    for n in range(3,N+1):
        dp[n]=max(dp[n-2]+A[n],dp[n-3]+A[n]+A[n-1])
    # print(dp)
    return dp[n]

N=int(read())
A=list()
dp=[0]*(N+1)
A.append(0)
for _ in range(N):
    A.append(int(read()))

print(bottom_up(N))