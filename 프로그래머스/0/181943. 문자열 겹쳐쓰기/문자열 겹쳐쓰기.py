def solution(my_string, overwrite_string, s):
    initial_part = my_string[:s]
    
    middle_part = overwrite_string
    
    final_part = my_string[s+len(overwrite_string):]
    result = initial_part + middle_part + final_part
    
    return result
