def solution(array, commands):
    answer = []
    
    for c in commands:
        i, j, k = c
        sliced_arr = array[i-1:j]
        sliced_arr.sort()
        
        answer.append(sliced_arr[k-1])
    return answer