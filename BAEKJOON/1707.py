import sys
sys.setrecursionlimit(10**8)
read=sys.stdin.readline

def dfs(node,ac,c):
    global ret
    
    if not visit[node]:
        visit[node]=True
        color[node]=c%2
    elif visit[node]:
    
        if ac==color[node]:
            ret+=1
        return 0

    for i in range(1,n+1):
        if edge[node][i]:
            dfs(i,color[node],c+1)

case_num=int(read())
for _ in range(case_num):
    n,m=map(int,read().split())
    edge=[[0]*(n+1) for _ in range(n+1)]
    visit=[False]*(n+1)
    color=[None]*(n+1)
    c=0
    ret=0
    for _ in range(m):
        v1,v2=map(int,read().split())
        edge[v1][v2]=1
        edge[v2][v1]=1

    for i in range(1,n+1):
        dfs(i,None,0)
    # print(color)    
    if ret>0:
        print('NO')
    else:
        print('YES')
