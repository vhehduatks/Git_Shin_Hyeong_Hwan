import sys

n = int(input())
s = [list(map(int, sys.stdin.readline().split())) for i in range(n)]
Matrix=list()
for line in s:
    Matrix.append(line[0])
Matrix.append(s[-1][-1])
Mul=0
while(len(Matrix)>2):
    temp=Matrix[1:-1]
    Max=max(temp)
    Mindex=Matrix.index(Max)
    Prev=Matrix[Mindex-1]
    Next=Matrix[Mindex+1]
    Mul+=Matrix.pop(Mindex)*Prev*Next

print(Mul)