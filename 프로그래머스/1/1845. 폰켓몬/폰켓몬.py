def solution(nums):
    dict = {}
    for n in nums:
        dict[n] = 1 

    pocketmons = len(dict)
    
    half_pocketmons = len(nums) // 2
    
    return min(pocketmons, half_pocketmons)


