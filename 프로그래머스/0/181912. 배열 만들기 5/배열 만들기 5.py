def solution(intStrs, k, s, l):
    answer = []
    for number in intStrs:
        part_number = number[s:s+l]
        part_number_int = int(part_number)
        
        if part_number_int > k:
            answer.append(part_number_int)
        
    return answer


# 1단계: 배열돌면서 s~l 까지 잘라내기
# 2단계: 크기비교하기(이때 문자열이면 int 형과 비교가 불가능하니까 int로 바꿔줌)
# 3단계: 크면 배열에 추가
