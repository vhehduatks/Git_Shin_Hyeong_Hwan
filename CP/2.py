import sys
read=sys.stdin.readline

N=int(read())
A=list(read().strip())
dp=[None]*51
def Top_down(ptr):
    if ptr==N-1:
        return 1
    if dp[ptr]:
        return dp[ptr]
    ret=0
    if A[ptr]=='0':
        return 0
    for i in range(1,3):
        if i+ptr<N:
            ret+= Top_down(ptr+i)
    dp[ptr]=ret
    return ret
print(Top_down(0))