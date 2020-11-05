a="aabbacccc"	
b="ababcdcdababcdcd"	
c="abcabcdede"	
d="abcabcabcabcdededededede"	
e="xababcdcdababcdcd"
f="a"
g="aaaaaaaaaa"
h="aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"



def solution(s):
    if len(s)==1:
        return 1
    line=list()
    for i in range(1,round(len(s)/2)+1):
        line.append([s[j:j+i]for j in range(0,len(s),i)])    

    len_list=list()
   
    for i in range(len(line)):
        overlap=1
        temp=list()
        for j in range(1,len(line[i])):
            if line[i][j]==line[i][j-1]:
                if j==len(line[i])-1:
                    overlap+=1
                    temp.append(overlap)
                    temp.append(line[i][j-1])
                    break
                overlap+=1
                continue

            if overlap==1:
                if j==len(line[i])-1:
                    temp.append(line[i][j-1])
                    temp.append(line[i][j])
                    break
                temp.append(line[i][j-1])
            elif overlap>1:
                if line[i][j]!=line[i][j-1] and j==len(line[i])-1:
                    temp.append(line[i][j])
                temp.append(overlap)
                temp.append(line[i][j-1])
                overlap=1

        len_list.append(temp)    

 

    minvalue=list()
    
    for value in len_list:
        result=0
        for i in range(len(value)):
            if isinstance(value[i],int):
                result+=len(str(value[i]))
            else:
                result+=len(value[i])    

        minvalue.append(result)

    return min(minvalue)


print(solution(h))
