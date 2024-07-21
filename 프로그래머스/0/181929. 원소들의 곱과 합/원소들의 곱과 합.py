def solution(num_list):
    total= 1 # 원소들의 곱
    num = 0 # 원소들의 합
    
    for i in num_list:
        total*=i
        num+=i
        
    if total < num**2:
        return 1
    else:
        return 0