def solution(my_string, is_suffix):
    
    suffix_length = len(is_suffix)
    
    if is_suffix in my_string[-suffix_length:]:
        return 1
    else:
        return 0
