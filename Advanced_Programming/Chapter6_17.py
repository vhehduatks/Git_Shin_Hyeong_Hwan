

population_A=(100,150,230,120,180,100,140,95,81,21,4)
population_B=(300,420,530,420,400,300,40,5,1,1,1)

class village_func:
    def __init__(self,village_population,village_name):
        self.population=village_population
        self.name=village_name

    def calc_voter(self):
        voter=sum(self.population[2:])
        print("마을{}에 보내야 할 투표용지는{}장 입니다.".format(self.name,voter))
        
        return voter

    def calc_aging(self):
        aging="%.3f"%(sum(self.population[7:])/sum(self.population))    
        print("마을{}의 고령화 정도는 {} 입니다.".format(self.name,aging))

        return float(aging) 

if __name__ == "__main__":
    
    Village_A=village_func(population_A,"A")
    Village_B=village_func(population_B,"B")
    Village_A.calc_voter()
    Village_B.calc_voter()
    Village_A.calc_aging()
    Village_B.calc_aging()
