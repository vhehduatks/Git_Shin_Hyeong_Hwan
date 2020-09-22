def Amicable_Numbers(num):
    amicable=[]

    for i in range(num):
        
        for j in range(i+1,num):
            
            val_1=sum(Divisors(i))
            val_2=sum(Divisors(j))

            if val_1==j and val_2==i:
                print("Find amicable :",i,",",j)
                amicable.append((i,j))

def Divisors(num):
    divisors=[]
    for i in range(1,num):
        if num%i==0:
            divisors.append(i)

    return divisors        

if __name__ == "__main__":
    Range_num=2000
    Amicable_Numbers(Range_num) 
       

    
