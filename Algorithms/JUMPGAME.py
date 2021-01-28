import sys
read=sys.stdin.readline

def jump(x,y):
    global cache
    global n
    global board

    # print(x,y)
    if out_range(x,y):
        return 0
    if (x==n-1 and y==n-1):
        return 1
    
    
    jumpval=board[y][x]
    # print(jumpval)
    if not(cache[y][x]==-1):
        return cache[y][x]
    cache[y][x]=(jump(x+jumpval,y) or jump(x,y+jumpval))
   
    return cache[y][x]

def out_range(x,y):
    if x>=n or y>=n:
        return True
    return False

case_num=int(read())
for _ in range(case_num):
    n=int(read())
    cache=[[-1]*n for _ in range(n)]
    board=list()
    for _ in range(n):
        line=list(map(int,read().strip().split()))
        board.append(line)
    print('YES' if jump(0,0) else 'NO')
    # print(cache)
 
    





