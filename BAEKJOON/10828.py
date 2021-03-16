import sys
read=sys.stdin.readline

class Stack:
    
    def __init__(self):
        self.stack=list()

    def size(self):
        ret=len(self.stack)
        return ret
    
    def push(self,i):
        self.stack.append(i)
    
    def empty(self):
        if len(self.stack)>0:
            return 0
        else:
            return 1

    def pop(self):
        if not self.empty():
            return self.stack.pop(-1)
        else:
            return -1
    
    def top(self):
        if not self.empty():
            return self.stack[-1]
        else:
            return -1

s=Stack()
N=int(read())
for _ in range(N):
    temp=read().split()
    if temp[0]=='push':
        s.push(int(temp[1]))
    elif temp[0]=='pop':
        print(s.pop())
    elif temp[0]=='size':
        print(s.size())
    elif temp[0]=='empty':
        print(s.empty())
    elif temp[0]=='top':
        print(s.top())