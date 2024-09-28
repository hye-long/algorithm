def solution(a, b):
    answer = int(str(a)+str(b))
    answer2 = 2*a*b
    
    if answer>=answer2:
        return answer
    else:
        return answer2