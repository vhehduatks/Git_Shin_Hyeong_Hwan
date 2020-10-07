import math

class Chapter_func:
    def __init__(self,nums):
        nums=nums.split(' ')
        try:
            self.nums=list(map(int,nums))
        except Exception as e:
            print("Wrong_value :",e)
      
    def mean_of_n(self):   
    #파이썬 소수점 표기법 '%.1f'%=소수점1자리까지 표시 << 리턴타입 str임 주의

        return float('%.1f'%(sum(self.nums)/len(self.nums)))

    def sum_of_n(self):
        
        return sum(self.nums)

    #https://dojang.io/mod/page/view.php?id=2285 파이썬 리스트 축약
    def __pow_func(self,num,Mean):
        temp=(num-Mean)

        return temp*temp

    # comprehension
    def sdev_of_n(self):
        Len=len(self.nums)
        Mean=self.mean_of_n()      
        temp=[self.__pow_func(x,Mean) for x in self.nums]

        return float('%.1f'%(sum(temp)/Len))

if __name__ == "__main__":
    Nums=input("n개의 정수를 입력하시오 :")
    Func_class=Chapter_func(Nums)
    print("합 :",Func_class.sum_of_n())
    print("평균 :",Func_class.mean_of_n())
    print("분산 :",Func_class.sdev_of_n())
    print("표준편차 :",'%.1f'%math.sqrt(Func_class.sdev_of_n()))
    
