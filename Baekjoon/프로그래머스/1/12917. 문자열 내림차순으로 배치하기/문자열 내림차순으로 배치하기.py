def solution(s):
    listed = list(s)
    listed.sort(reverse=True)
    
    answer = ''.join(listed)
    
    return answer

