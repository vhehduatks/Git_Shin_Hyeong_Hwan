import sys
read=sys.stdin.readline

def path(x,y):
    global cachep
    global tri
    global n

    if y==n-1:
        return tri[y][x]

    if cachep[y][x]:
        return cachep[y][x]
    
    ret=0
    weight=tri[y][x]

    ret=max(path(x,y+1)+weight,path(x+1,y+1)+weight)
    
    cachep[y][x]=ret
    
    return ret

def count(x,y):
    global cachec
    global n

    if y==n-1:
        return 1
    
    if cachec[y][x]:
        return cachec[y][x]

    ret=0

    if path(x,y+1)>=path(x+1,y+1):
        ret+=count(x,y+1)

    if path(x,y+1)<=path(x+1,y+1):
        ret+=count(x+1,y+1)

    cachec[y][x]=ret
    return ret

case_num=int(read())

for _ in range(case_num):
    n=int(read())
    cachep=[[None]*(n+1) for _ in range(n+1)]
    cachec=[[None]*(n+1) for _ in range(n+1)]
    tri=list()
    for _ in range(n):
        temp=list(map(int,read().split()))
        tri.append(temp)
    # print(tri)
    # print(cachec)
    print(count(0,0))
    
    