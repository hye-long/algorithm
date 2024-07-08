def solution(x):
    number = 0

    for i in str(x):
        number+=int(i)
        
    if x % number == 0:
        return True
    else:
        return False
    
   