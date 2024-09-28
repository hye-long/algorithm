def solution(n):
    answer = []  
    while n != 1:  
        answer.append(n)  
        if n % 2 == 0: 
            n = n // 2  # n을 2로 나눔
        else:  # n이 홀수일 경우
            n = 3 * n + 1  # n을 3 * n + 1로 변경
    answer.append(1)  # 마지막 값 1을 리스트에 추가
    return answer  