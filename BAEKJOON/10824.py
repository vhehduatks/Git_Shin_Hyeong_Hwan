import sys
read=sys.stdin.readline

A=read().strip().split()
front=A[0]+A[1]
back=A[2]+A[3]
print(int(front)+int(back))