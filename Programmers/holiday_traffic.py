import math as m
import datetime as d
lines=["2016-09-15 20:59:57.421 0.351s",
"2016-09-15 20:59:58.233 1.181s",
"2016-09-15 20:59:58.299 0.8s",
"2016-09-15 20:59:58.688 1.041s",
"2016-09-15 20:59:59.591 1.412s",
"2016-09-15 21:00:00.464 1.466s",
"2016-09-15 21:00:00.741 1.581s",
"2016-09-15 21:00:00.748 2.31s",
"2016-09-15 21:00:00.966 0.381s",
"2016-09-15 21:00:02.066 2.62s"
]
lines1=	["2016-09-15 01:00:04.001 2.0s", "2016-09-15 01:00:07.000 2s"]


today = d.datetime.today()

t=today + d.timedelta(days=1)

def solution(lines):

    split_line=[]

    for line in lines:
        temp=line.split(" ")
        temp_string0=temp[0]
        temp_string1=temp[1]
        temp_string2=temp[2]
        split_line.append((temp_string1,temp_string2))

    task_start_end=[]
    for test1,test2 in split_line:
        
        time1=d.datetime.strptime(test1,'%H:%M:%S.%f')-d.datetime(1900,1,1)#끝시간
 
        test2=test2.strip("s")#걸린시간
        if "." in test2:
            time2=(d.datetime.strptime(test2,"%S.%f"))-d.datetime(1900,1,1)-d.timedelta(milliseconds=1)
        else:
            time2=(d.datetime.strptime(test2,"%S"))-d.datetime(1900,1,1)-d.timedelta(milliseconds=1)   
        time3=time1-time2# 시작시간 
        print(" ",time3,time1)
        task_start_end.append([time3,time1])           

    max_count=[]
    for i in task_start_end:
       
        for start in i:
            count=0
            end=start+d.timedelta(milliseconds=999)
            for temp_st,temp_ed in task_start_end:
                if start<=temp_st and temp_st<=end and end<=temp_ed:
                    count+=1
                    print("범위안1:",temp_st,"~",temp_ed) 
                elif temp_st<=start and start<=temp_ed and temp_ed<=end:
                    count+=1
                    print("범위안2:",temp_st,"~",temp_ed)
                elif start<=temp_st and temp_ed<=end:
                    count+=1
                    print("범위안3:",temp_st,"~",temp_ed)
                elif temp_st<=start and end<=temp_ed:
                    count+=1
                    print("범위안4:",temp_st,"~",temp_ed)
                  

            max_count.append(count)
            print(start,end)    

        
        
        
        
    print(max_count)

        
    
    
    return max(max_count)

solution(lines1)