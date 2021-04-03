import sys
read=sys.stdin.readline

def A(Str):
    temp=list()
    ptr=0
    while ptr<len(Str):
        s=Str[ptr:]
        temp.append(s)
        ptr+=1
    temp.sort()
    return temp

B=A(read().strip())

for i in B:
    print(i)