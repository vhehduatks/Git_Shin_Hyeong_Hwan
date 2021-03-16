import sys
read=sys.stdin.readline

class Q:
    
    def __init__(self):
        self.q=list()

    def push(self,i):
        self.q.append(i)

    def pop(self):
        if not self.empty():
            return self.q.pop(0)
        else:
            return -1

    def size(self):
        ret=len(self.q)
        return ret
    
    def empty(self):
        if len(self.q)>0:
            return 0
        else:
            return 1

    def front(self):
        if not self.empty():
            return self.q[0]
        else:
            return -1

    def back(self):
        if not self.empty():
            return self.q[-1]
        else:
            return -1

q=Q()
N=int(read())
for _ in range(N):
    temp=read().split()
    if temp[0]=='push':
        q.push(int(temp[1]))
    elif temp[0]=='pop':
        print(q.pop())
    elif temp[0]=='size':
        print(q.size())
    elif temp[0]=='empty':
        print(q.empty())
    elif temp[0]=='front':
        print(q.front())
    elif temp[0]=='back':
        print(q.back())