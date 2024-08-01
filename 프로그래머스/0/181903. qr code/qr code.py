def solution(q, r, code):
    answer = ""
    
    for i in range(len(code)):
        if i % q == r:
            answer += code[i]

    return answer


# 1. 각 인덱스 돌기
# 2. 각 인덱스를 q 로 나누어서 나머지 계산
# 3. 나머지가 r과 같은 경우 ->> 해당 인덱스의 문자를 결과문자열에 추가
