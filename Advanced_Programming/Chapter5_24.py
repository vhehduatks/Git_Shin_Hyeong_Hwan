def Divisors(num):
   
    divisors=list()
# 항상 범위 생각할것
    for i in range(1,num+1):
        if num%i==0:
            divisors.append(i)

    return divisors

def Perfect_Numbers(num):
    
    perfect_nums=list()
    for i in range(2,num):
        temp=Divisors(i)
        
        if temp.pop()==sum(temp):
            print("Find perfect num :",sum(temp),"show list :",temp,"sum of divisors :",sum(temp))
            perfect_nums.append(sum(temp))
    
    return perfect_nums

if __name__=="__main__":
    Range_num=10000
    Perfect_Numbers(Range_num)