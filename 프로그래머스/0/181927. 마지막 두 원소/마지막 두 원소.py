def solution(num_list):
    if num_list[-1] > num_list[-2]:
        a = num_list[-1] - num_list[-2]
        num_list.append(a)
    else:
        b = num_list[-1] * 2
        num_list.append(b)
    
    return num_list