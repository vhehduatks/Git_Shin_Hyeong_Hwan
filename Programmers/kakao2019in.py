
s="{{4,2,3},{3},{2,3,4,1},{2,3}}"

def solution(s):
    temp=s[2:-2]
    temp2=temp.split("},{")
    temp3=[]
    for x in temp2:
        temp3.append(list(map(int,x.split(","))))
    
    temp3=sorted(temp3,key=len)

    answer=[]

    for i in temp3:
        for j in i:
            if j not in answer:
                answer.append(j)
    
    return answer

print(solution(s))