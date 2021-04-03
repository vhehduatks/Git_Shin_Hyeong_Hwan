import sys
read=sys.stdin.readline
size=int(read())
A=list()
def squre_ok(px,py,n,size):
    for x in range(n):
        for y in range(n):
            if py+y>=size or px+x>=size:
                return False
            if A[py+y][px+x]==0:
                return False
    return True

def BP(A):
    temp=list()
    for N in range(1,size+1):
        ret=0
        for x in range(size):
            for y in range(size):
                if squre_ok(x,y,N,size):
                    ret+=1
        temp.append(ret)
    return temp

for _ in range(size):
    line=list(read().strip())
    line=list(map(int,line))
    A.append(line)


ret=BP(A)
print('total: '+str(sum(ret)))
for i in range(len(ret)):
    if not ret[i]==0:
        print('size['+str(i+1)+']: '+str(ret[i]))