import sys
read=sys.stdin.readline
INF=float('inf')
N,M=map(int,read().split())

A=list()
for _ in range(M):
    line=list(read().strip())
    A.append(line)

def check(px,py):
    if 0<=px and px<N:
        if 0<=py and py<M:
            if not A[py][px]=='x':
                return True
    return False

dp=[[None]*21 for _ in range(1001)]
def recur(x,y):
    ret=INF
    if y==M-1:
        return 0
    if dp[y][x]:
        return dp[y][x]
    if check(x,y):
        ret=min(recur(x,y+1),recur(x+1,y)+1,recur(x-1,y)+1)
    dp[y][x]=ret
    return ret

print(recur(3,0))