import sys
import datetime as dt
read=sys.stdin.readline

N=int(read())
A=list()
for _ in range(N):
    time=read().strip().split(' ~ ')
    A.append(time)
B=list()
mintime=dt.datetime.strptime('23:59','%H:%M')
maxtime=dt.datetime.strptime('00:00','%H:%M')
for a in A:
    maxtime=max(maxtime,dt.datetime.strptime(a[0],'%H:%M'))
    mintime=min(mintime,dt.datetime.strptime(a[1],'%H:%M'))

if maxtime<mintime:
    ret=str(dt.datetime.strftime(maxtime,'%H:%M'))+' ~ '+str(dt.datetime.strftime(mintime,'%H:%M'))
    print(ret)
else:
    print(-1)

