import sys
read=sys.stdin.readline

def dfs(node):
    visit[node]=True
    for Next in edge[node]:
        if not visit[Next]:
            dfs(Next)

case_num=int(read())
for _ in range(case_num):
    cycle=0
    n=int(read())
    visit=[False]*(n+1)
    v=list(map(int,read().split()))
    v.insert(0,0)
    edge=[[] for _ in range(n+1)]
    for i in range(1,len(v)):
        edge[i].append(v[i])
        edge[v[i]].append(i)
    
    for i in range(1,n+1):
        if visit[i]==False:
            dfs(i)
            cycle+=1
    print(cycle)
