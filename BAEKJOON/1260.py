import sys
sys.setrecursionlimit(10**8)
read=sys.stdin.readline

n,m,v=map(int,read().split())

edge=[[0]*(n+1) for _ in range(n+1)]
new_edge=[[] for _ in range(n+1)]

visit_D=[False]*(n+1)
visit_B=[False]*(n+1)
Q=list()
for _ in range(m):

    v1,v2=map(int,read().split())
    new_edge[v1].append(v2)
    new_edge[v2].append(v1)
    edge[v1][v2]=1
    edge[v2][v1]=1

def dfs(node):

    visit_D[node]=True
    print(node,end=' ')
    for i in range(1,n+1):
        if visit_D[i]==False and edge[node][i]:
            dfs(i)

def bfs(node):

    visit_B[node]=True
    print(node,end=' ')
    for i in range(1,n+1):
        if visit_B[i]==False and edge[node][i] and not(i in Q):
            Q.append(i)
        
    if Q:
        bfs(Q.pop(0))

visit=[False]*(n+1)
def new_bfs(node):
    visit[node]=True
    print(node,end=' ')

    for Next in new_edge[node]:
        if visit[Next]==False and not(Next in Q):
            Q.append(Next)
    if Q:
        new_bfs(Q.pop(0))

dfs(v)
print('')
bfs(v)
print('')
new_bfs(v)



