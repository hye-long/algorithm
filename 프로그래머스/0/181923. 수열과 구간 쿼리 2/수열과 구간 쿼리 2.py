def solution(arr, queries):
    results = []
    
    for query in queries:
        s = query[0]
        e = query[1]
        k = query[2]
        
        answer = [arr[i] for i in range(s, e + 1) if arr[i] > k]
        

        if answer:
            results.append(min(answer))
        else:
            results.append(-1)
    
    return results