import sys
sys.setrecursionlimit(10**8)
read=sys.stdin.readline

def dfs(node):
    visit[node]=True

    for i in range(1,n+1):
        if visit[i]==False and edge[node][i]:
            dfs(i)

n,m=map(int,read().split())
edge=[[0]*(n+1) for _ in range(n+1)]
visit=[False]*(n+1)
ret=0
for _ in range(m):
    v1,v2=map(int,read().split())
    edge[v1][v2]=1
    edge[v2][v1]=1

for i in range(1,n+1):
    if visit[i]==False:
        ret+=1
        dfs(i)
print(ret)