v=[[1, 1], [2, 2], [1, 2]]
v2=[[1, 4], [3, 4], [3, 10]]
def solution(v):
    x=list()
    y=list()
    for i in range(len(v[0])):
        for j in range(len(v)):
            if i==0:
                x.append(v[j][i])
            elif i==1:
                y.append(v[j][i])  

    print(y)
    result=list()
    try:
        remove=x.index(x[0],1)
        x.pop(remove)
        x.pop(0)
        result.append(x[0])   
    except Exception:
        result.append(x[0])
                
    try:
        remove=y.index(y[0],1)
        y.pop(remove)
        y.pop(0)
        result.append(y[0])   
    except Exception:
        result.append(y[0])
            

    return result

print(solution(v2))    