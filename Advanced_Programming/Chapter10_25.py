
#람다는 리턴을 하므로 항상 리턴할 수 있는 값 ex 리스트,값
#all 함수는 empty 입력시 true 리턴
is_prime=lambda x: all([x%i!=0 for i in range(2,int(x/2))])

print(is_prime(12))
print(is_prime(11))



prime_nums=lambda m,n: list(filter(is_prime,[i for i in range(m,n+1)]))
print(prime_nums(1,50))
