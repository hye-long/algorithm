def solution(a, d, included):
    answer = 0
    for i in range(len(included)):
        if included[i] == True:
            term = a + i * d  # 등차수열 적용
            answer += term # True 인 애들만 더함
    return answer
    

