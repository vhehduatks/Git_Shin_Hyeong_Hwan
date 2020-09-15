class Basel_Problem:
    def __init__(self, int_val):
        self.Integer = int_val
        self.temp=0
        
    def __clac(self, int_val):
        if self.Integer<=0:
            return -1  
        if self.Integer==self.temp:
            return (1/self.temp)**2 
        self.temp+=1
        result=(1/self.temp)**2
        print("result :",result)
        return result+self.__clac(self.temp)

    def __str__(self):
        return str(self.__clac(self.Integer))

if __name__ == "__main__":
    # 형변환 확인할것
    try:
        main_func = Basel_Problem(int(input("정수를 입력하세요 :")))
        print(main_func)
    except ValueError as e:
        print(e, "Wrong Value")

    
