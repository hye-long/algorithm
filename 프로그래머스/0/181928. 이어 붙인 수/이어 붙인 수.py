def solution(num_list):
    odd = []
    even = []
    
    for i in num_list:
        if i % 2 == 0:
            even.append(str(i))
        else:
            odd.append(str(i))
            
    odd_number = int(''.join(odd)) 
    even_number = int(''.join(even)) 
    return odd_number + even_number
