def solution(clothes):
    answer = 1
    
    closet = {}
    for types, val in clothes:
        if val in closet:
            closet[val].append(types)
        else:
            closet[val] = [types]
    
    for types in closet.values():
        answer *= (len(types)+1)
    
    return answer - 1
