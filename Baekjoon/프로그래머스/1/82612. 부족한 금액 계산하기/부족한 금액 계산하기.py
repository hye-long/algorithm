def solution(price, money, count):
    cost=0
    
    for i in range(1, count+1):
        cost += price*i
        
    total_price= money - cost
    
    if total_price >0:
        return 0
    
    else:
        return abs(total_price)  
    
