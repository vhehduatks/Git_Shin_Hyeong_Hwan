import string

class Caesar_code:
    def __init__(self,input_str,input_num=0):
            self.src_str_up=string.ascii_uppercase
            self.src_str_low=string.ascii_lowercase
            self.input_str=input_str
            self.input_num=input_num  
#파이썬 절대값 abs   
    def Shift(self,str_value,shift_val):
        if(isinstance(shift_val,int)==False):
            return -1

        shift_val*=-1
        return_str=str_value[shift_val:]+str_value[:shift_val]

        return return_str

    def ciper_en(self):
        dst_str_up=self.Shift(self.src_str_up,self.input_num)
        dst_str_low=self.Shift(self.src_str_low,self.input_num)
        encode=''
        for x in self.input_str:
            encode+=self.Encode_str(x,dst_str_low,dst_str_up)
        print("Encode string :",encode)    
        return encode
    
    def ciper_de(self,encode_str):
        dst_str_up=self.Shift(self.src_str_up,self.input_num)
        dst_str_low=self.Shift(self.src_str_low,self.input_num)
        decode=''
        for x in encode_str:
            decode+=self.Decode_str(x,dst_str_low,dst_str_up)
        print("Decode string :",decode)    
        return decode         

    def Encode_str(self,target_str,dst_str_low,dst_str_up):
       
        if str(target_str).islower():
            
            src_index=self.src_str_low.find(target_str)
            return dst_str_low[src_index]
        elif str(target_str).isupper():
            src_index=self.src_str_up.find(target_str)

            return dst_str_up[src_index]
        else:
            return target_str        

    def Decode_str(self,target_str,dst_str_low,dst_str_up):
               
        if str(target_str).islower():
            
            dst_index=dst_str_low.find(target_str)
            return self.src_str_low[dst_index]
        elif str(target_str).isupper():
            dst_index=dst_str_up.find(target_str)

            return self.src_str_up[dst_index]
        else:
            return target_str  
        

if __name__ == "__main__":
    Caesar=Caesar_code("Hello World!",-3)
    Encode_str=Caesar.ciper_en()
    Decode_str=Caesar.ciper_de(Encode_str)      

        
