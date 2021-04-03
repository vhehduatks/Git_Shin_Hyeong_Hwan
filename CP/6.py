import sys
read=sys.stdin.readline

nx,ny=map(int,read().split())
A=list()
for _ in range(ny):
    line=list(map(int,read().split()))
    A.append(line)

dp=[[None]*101 for _ in range(10001)]
def path(x,y):
    if dp[y][x]:
        return dp[y][x]
    
    if x==nx-1 and y==ny-1:
        return A[ny-1][nx-1]
    ret=0

    if x+1<nx and y+1<ny:
        ret=max(path(x+1,y)+A[y][x],path(x,y+1)+A[y][x])

    elif y+1==ny:
        ret+=path(x+1,y)+A[y][x]
    elif x+1==nx:
        ret+=path(x,y+1)+A[y][x]

    dp[y][x]=ret
    return ret
print(path(0,0))