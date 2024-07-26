def solution(my_string):
    answer=[]
    for word in range(len(my_string)):
        answer.append(my_string[word:])

    answer.sort()
    return answer

# 1. 정렬
# 2. 하나씩 늘려가면서 ~..~ => 인덱스를 하나씩 넣으면 되는거임 