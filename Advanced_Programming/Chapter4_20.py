def fibo(num):
    F=[0]*num
    if num>0:
        F[1]=1
        for i in range(2,num):
            F[i]=F[i-1]+F[i-2]

    return F
   
if __name__ == "__main__":
    max_num=15
    Fibo_num=fibo(max_num+1)

    for i in range(max_num+1):
        print("Fibo( {}) =  {}".format(i,Fibo_num[i]))
