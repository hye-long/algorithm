def solution(n, k):
    answer = []
    i = 1
    while k * i <= n:
        answer.append(k * i)
        i += 1
    
    return answer

#1. 배수니까 1부터 시작하는 애를 
# 반복문 안에서 계속해서 곱해지게 만들어서 반환
