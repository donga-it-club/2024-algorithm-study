def solution(progresses, speeds):
    n = len(progresses)
    days = [0] * n
    
    for i in range(n):
        remain = 100 - progresses[i]
        days[i] = (remain + speeds[i] - 1) // speeds[i]
    
    result = []
    current_max_day = days[0]
    count = 0
    
    for day in days:
        if day <= current_max_day:
            count += 1
        else:
            result.append(count)
            current_max_day = day
            count = 1
    result.append(count)  
    
    return result
