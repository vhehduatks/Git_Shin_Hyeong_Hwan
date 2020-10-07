class String_func:
    def __init__(self,str_value):
        self.Str=list(str_value) 
 

    def encode(self):
        temp=1
        end_index=len(self.Str)
        e_newlist=list()
        for i in range(end_index-1):
            if(self.Str[i]==self.Str[i+1]):
                temp=temp+1
            else:
                e_newlist.append(self.Str[i])
                e_newlist.append(temp)
                temp=1
            """
            i의 범위가 0~<end_index-1이므로 n열의 문자는 n-1까지 참고할수 있다.
            i가 n-1번째 문자를 가르킬때 i+1는 n번째 문자를 가르키며 
            i의 값이 end_index-2 일때 n번째 문자까지의 temp가 결정되므로 
            마지막 문자의 조건은 
            i이 end_index-2과 동일해질 때이다.
            """
            if i==end_index-2 and temp==1:
                e_newlist.append(self.Str[i+1])
                e_newlist.append(temp)
            elif i==end_index-2 and temp!=1:
                e_newlist.append(self.Str[i])
                e_newlist.append(temp)        


        return e_newlist

    def decode(self,nlist):
        end_index=len(nlist)
        if end_index%2!=0:
            print("worng_list")
            return -1

        d_newlist=list()
        for i in range(int(end_index/2)):
            temp=nlist[i*2+1]
            for j in range(temp):
                d_newlist.append(nlist[i*2])    

        return d_newlist


    def func_print(self,nlist):
        print(nlist)
        if isinstance(nlist,list):
            for x in nlist:
                print(x,end='')
            print('')
        else:
            print("worng value")     





#for 문 enumerate 으로 인덱스와 동시 접근가능
if __name__ == "__main__":
    String=input("임의의 문자열을 입력하시오 :")
    func=String_func(String)
    encode_list=func.encode()
    func.func_print(encode_list)
    decode_list=func.decode(encode_list)
    func.func_print(decode_list)
  