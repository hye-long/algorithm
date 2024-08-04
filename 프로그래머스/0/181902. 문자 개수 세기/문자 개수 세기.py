def solution(my_string):
    answer = [0] * 52
    upper_case = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    lower_case = 'abcdefghijklmnopqrstuvwxyz'
    
    for char in my_string:
        for i in range(26):
            if char == upper_case[i]:  
                answer[i] += 1
            elif char == lower_case[i]:  
                answer[i + 26] += 1
    
    return answer
