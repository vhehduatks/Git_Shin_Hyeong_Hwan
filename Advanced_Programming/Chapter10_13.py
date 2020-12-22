def leap(start,end):
    
    #using lambda and filter 
    leap_list1=list(filter(lambda x:(x%4==0 and x%100!=0)or(x%400==0),[x for x in range(start,end+1)]))

    #list comprehension
    leap_list2=[x for x in range(start,end+1) if (x%4==0 and x%100!=0)or(x%400==0)]
    
    return leap_list1,leap_list2

print(leap(2001,2030))
        