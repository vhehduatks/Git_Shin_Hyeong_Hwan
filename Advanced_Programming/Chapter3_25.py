class Snail:
    #달팽이가 14시간동안 우물을 오르고 10시간동안 취침한다고 가정
    def __init__(self):
        self.init_point=0
        self.date=1
        
       
    def work(self,time):
        if self.init_point>30:
            print(self.date,"일차 ""달팽이가 우물에서 탈출했습니다. 현제 시각은 ",time,"시 입니다.")
            return 0
        #24==00시이므로 0시엔 달팽이가 자고있음
        if time>0 and time<=14:
            print(self.date,"일차 ""현제 시각",time,"시 달팽이가 우물을 오르는 중입니다. ",end='')
            self.init_point+=7/14
            print("달팽이의 위치는 :",self.init_point,"미터 입니다.")
        else:
            self.__sleep(time)

    def __sleep(self,time):
        if time>14 and time<=24:
            print(self.date,"일차 ""현제 시각",time,"시 달팽이가 자고 있는중입니다.",end='')
            self.init_point-=5/10
            print("달팽이의 위치는 :",self.init_point,"미터 입니다.") 
        if time==24:
            self.date+=1       

    

if __name__ == "__main__":
    Time=0
    snail=Snail()
    while(1):
        if snail.work(Time)==0:
            break
        if Time==24:
            Time=0
        Time+=1