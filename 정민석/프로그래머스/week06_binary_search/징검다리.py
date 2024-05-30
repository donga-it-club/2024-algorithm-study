def solution(distance, rocks, n):
    rocks.sort()
    rocks = [0] + rocks + [distance]
    
    left, right = 1, distance
    
    while left <= right:
        mid = (left + right) // 2
        current = 0
        removed_rocks = 0
        
        for i in range(1, len(rocks)):
            if rocks[i] - rocks[current] < mid:
                removed_rocks += 1
            else:
                current = i
        
        if removed_rocks > n:
            right = mid - 1
        else:
            left = mid + 1
            
    return right
