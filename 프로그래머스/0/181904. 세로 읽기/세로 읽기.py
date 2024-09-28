def solution(my_string, m, c):
    # c번째 열의 문자들을 추출
    answer = ''.join(my_string[i] for i in range(c-1, len(my_string), m))
    return answer


# 한 줄에 m 글자씩 나누기 
# c열에 적힌 글자 찾기
# 세로로 읽기 
