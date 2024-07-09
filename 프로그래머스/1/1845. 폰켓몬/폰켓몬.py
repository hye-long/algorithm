def solution(nums):
    unique_nums = set(nums)
    return min(len(nums) // 2, len(unique_nums))


