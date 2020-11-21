
def solution(bridge_length, weight, truck_weights):
    count=0  
    truck_w=[]
    truck_time=[]    
    while(len(truck_weights)>0 or len(truck_w)>0):
        count+=1
        truck_len=len(truck_weights)
        if truck_len>0:
            truck_pop=truck_weights.pop(0)
        print(truck_pop)
        if len(truck_time)>0:
            truck_time=list(map(lambda x:x-1,truck_time))
            if truck_time[0]==0:
                truck_w.pop(0)
                truck_time.pop(0)

        if ((sum(truck_w)+truck_pop<=weight)and(truck_len>0)):
            truck_w.append(truck_pop)
            truck_time.append(bridge_length)
        elif((sum(truck_w)+truck_pop>weight)and(truck_len>0)):
            truck_weights.insert(0,truck_pop)
        
        
       
        
        print(count)
        print(truck_weights)

        print(truck_w)
        print(truck_time)  
    return count

bridge_length=100   
weight=100
truck_weights=[10]
print(solution(bridge_length,weight,truck_weights))