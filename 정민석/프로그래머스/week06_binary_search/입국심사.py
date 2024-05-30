def solution(n, times):
    min_time = min(times) # 가능한 최소 시간
    max_time = max(times) * n #가능한 최대시간, 가장 오래 걸리는 심사관이 모든 사람을 심사하는 case
    
    #이진 탐색
    while min_time <= max_time:
        mid_time = (min_time + max_time) // 2
        total_people = sum(mid_time // time for time in times)
        
        if total_people >= n:
            max_time = mid_time - 1
        else:
            min_time = mid_time + 1
            
    return min_time
