def solution(citations):
    answer = 0
    
    citations.sort(reverse=True)
    for i, citations in enumerate(citations):
        answer = max(answer,min(citations, i + 1))
        

    return answer