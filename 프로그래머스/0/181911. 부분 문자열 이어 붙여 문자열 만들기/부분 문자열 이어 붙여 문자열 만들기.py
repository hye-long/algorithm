def solution(my_strings, parts):
    answer =""
    for word in range(len(my_strings)):
        s, e = parts[word]
        words = my_strings[word][s:e+1]
        
        answer+=words
        
    return answer

# s부터 e까지의 부분 문자열을 추출
# 추출한 부분 문자열을 순서대로 이어붙임
