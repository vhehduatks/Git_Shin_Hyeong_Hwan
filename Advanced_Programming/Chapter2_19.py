def Odd_func():    

    while(1):
        try:
            val_A=int(input("input INTEGER(-1=end func) :"))
            print("입력된 정수는 0이상 100이하의 짝수입니까? :",end='')
            if val_A>=0 and val_A<=100 :
                print("True")
            elif val_A==-1:
                break
            else:
                print("False")      
        except ValueError as e:
            print(e,"올바른 값을 입력해 주세요")                        

Odd_func()