from collections import defaultdict

def solution(clothes):
    answer = 1
    closet = defaultdict(list)

    for item, type in clothes:
        closet[type].append(item)

    for count in closet.values():
        answer *= (len(count) + 1)

    return answer - 1

