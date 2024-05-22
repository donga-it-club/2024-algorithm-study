def dfs(numbers, target, index, current_sum):
    # 모든 숫자를 다 사용했을 경우 핸들링
    if index == len(numbers):
        return 1 if current_sum == target else 0
    
    # 현재 숫자를 더하는 경우와 빼는 경우를 각각 탐색
    count_with_plus = dfs(numbers, target, index + 1, current_sum + numbers[index])
    count_with_minus = dfs(numbers, target, index + 1, current_sum - numbers[index])
    
    # 두 경우의 수를 합산후 반환
    return count_with_plus + count_with_minus

def solution(numbers, target):
    return dfs(numbers, target, 0, 0)



