
#A with statement does not create a scope

with open('num10.txt','r') as f:
  
    # temp=list()
    # for line in f:
    #     temp.append(line.strip())
    # print(temp)
    # f.seek(0)
    
    #seek(0) 으로 포인터를 되돌릴수 있음.
    #입력시 개행문자 생각할것
    temp=list(map(lambda x: int(x.strip()),f.readlines()))
    # f.seek(0)
    # f.truncate(0)


with open('numby10.txt','w') as f:
    for i in temp:
        f.write(str(i*10)+"\n")





