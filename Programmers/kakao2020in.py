#(List comprehension)https://wikidocs.net/22#2-for

expr="100-200*300-500+20"
def solution(expression):
    seps=["+","-","*"]
    d_sep=seps[0]

    string=list(expression)
    opers=[]
    for x in string:
        if x in seps:
            opers.append(x)
    
    # print(opers)#1,3,5,7..


    for sep in seps[1:]:
        expression=expression.replace(sep,d_sep)

    temp=[i.strip() for i in expression.split(d_sep)]


    # print(temp)#0,2,4,6,8..
    
    new_list=[]
    new_list.append(temp[0])
    for i in range(len(opers)):
        new_list.append(opers[i])
        new_list.append(temp[i+1])
    # print(new_list)

    calc(seps,new_list)


    answer = 0
    return answer


def calc(sep,nlist):
    result=0
    index_list=[]
    clac_list=[]
    for i in sep:
        index_p=0
        index_list_temp=[]
        
        for _ in range(len(sep)):
            try:
                index_p=nlist.index(i,index_p)
                string=nlist[index_p-1]+nlist[index_p]+nlist[index_p+1]
                print(string)
                clac_list.append(eval(string))
                nlist.insert(index_p,eval(string))
                print("삽입후 ",nlist)
                del nlist[index_p+1]
                del nlist[index_p+2]
                del nlist[index_p-1]
                # del nlist[index_p+2]
                print("제거후 ",nlist)
                index_list_temp.append(index_p)
                index_p+=1
            except Exception:
                print("예외")
                continue  
        index_list.append(index_list_temp)
       
    
    print(index_list)
    print(clac_list)
        
        
        
solution(expr)         
