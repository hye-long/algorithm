def solution(my_string, indices):
    indices = sorted(indices, reverse=True)  
    
    for i in indices:
        my_string = my_string[:i] + my_string[i+1:]  
    
    return my_string


# 이미 indices 는 literable 이니까 걍 in
# indice배열을 받는데 너무 난잡하게 되어있으니까 순서를 정렬해줌 
# 문자열이기 때문에 정렬된 애들 잘라서 강 + 로 붙여주기 