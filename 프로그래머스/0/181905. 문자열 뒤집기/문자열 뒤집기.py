def solution(my_string, s, e):
    pre_string = my_string[:s]
    real_string = my_string[s:e+1][::-1]
    last_string = my_string[e+1:]
    
    answer = pre_string + real_string + last_string
    return answer
