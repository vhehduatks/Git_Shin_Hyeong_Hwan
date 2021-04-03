import sys
import string
read=sys.stdin.readline
word=read().strip()
Ascii=string.ascii_lowercase
ret=[0]*(26)

for a in word:
    idx=Ascii.index(a)
    ret[idx]+=1

for r in ret:
    print(r,end=' ')
