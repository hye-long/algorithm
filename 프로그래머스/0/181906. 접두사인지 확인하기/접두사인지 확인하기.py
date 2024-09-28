def solution(my_string, is_prefix):
    
    prefix_length = len(is_prefix)
    
    if is_prefix in my_string[0:prefix_length]:
        return 1
    else:
        return 0