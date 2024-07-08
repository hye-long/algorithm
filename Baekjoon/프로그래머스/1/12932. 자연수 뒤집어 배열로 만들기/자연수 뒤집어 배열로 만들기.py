def solution(n):
    num=str(n)
    reversed_num=[]
    
    for digit in reversed(num):
        reversed_num.append(int(digit))
    
    return reversed_num