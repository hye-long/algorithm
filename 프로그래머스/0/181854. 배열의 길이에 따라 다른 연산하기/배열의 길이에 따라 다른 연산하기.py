def solution(arr, n):
    for a, b in enumerate(arr):
        if len(arr) % 2 == 0:
            if a % 2 == 1:
                arr[a] += n
        else:
            if a % 2 == 0:
                arr[a] += n
    
    return arr