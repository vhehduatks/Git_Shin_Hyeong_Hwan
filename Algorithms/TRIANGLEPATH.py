import sys
read=sys.stdin.readline

# cache=[]
# tri=[]
# size=0
def path(x,y):
    global cache
    global tri
    global size
    if not(cache[y][x]==-1):
        return cache[y][x]

    if y==size-1:
        return tri[y][x]

    cache[y][x]=max(path(x,y+1),path(x+1,y+1))+tri[y][x]
    
    return cache[y][x]

cs=int(read())
for _ in range(cs):
    size=int(read())
    tri=[]
    cache=[[-1]*size for _ in range(size)]
    for _ in range(size):
        line=list(map(int,read().split()))
        tri.append(line)
    print(path(0,0))
    
    # print(cache)