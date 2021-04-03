import sys
import string
read=sys.stdin.readline
word=read().strip()
Ascii=string.ascii_lowercase
ret=[-1]*(26)
ptr=0

for a in word:
    idx=Ascii.index(a)
    if ret[idx]==-1:
        ret[idx]=ptr
    ptr+=1

for r in ret:
    print(r,end=' ')
