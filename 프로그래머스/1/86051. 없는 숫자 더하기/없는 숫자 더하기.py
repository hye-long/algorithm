def solution(numbers):
    total = 0
    find = [0,1,2,3,4,5,6,7,8,9]
    for i in find:
        if i not in numbers:
            total += i
        
    return total 
        

#1) 5+9 = 14
#2) 1+2+3= 6 