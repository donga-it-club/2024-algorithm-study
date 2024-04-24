def solution(nums):
    num_types = len(set(nums)) 
    num_choice = len(nums) // 2 
    
    return min(num_types, num_choice)
