class temp_convert:
    def __init__(self,cel_list):
        self.cel_list=cel_list
    
    def convert(self,celsius):
        return (9/5)*celsius+32

    def print_convert(self):
        print("섭씨\t\t화씨")
        for cel in self.cel_list:
            print("{}\t\t{}".format(cel,self.convert(cel)))

if __name__ == "__main__":
    Celsius_list=[0,10,20,30,40,50]
    Converter=temp_convert(Celsius_list)
    Converter.print_convert()
