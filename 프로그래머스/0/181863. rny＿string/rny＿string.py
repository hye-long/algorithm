def solution(rny_string):
    answer = ['rn' if x == 'm' else x for x in rny_string]
    return ''.join(answer)