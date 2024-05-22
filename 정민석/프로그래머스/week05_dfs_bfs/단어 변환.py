from collections import deque

#bfs
def is_transformable(word1, word2):
    # 두 단어가 한 글자만 다른지 확인
    count = sum([1 for a, b in zip(word1, word2) if a != b])
    return count == 1

def solution(begin, target, words):
    if target not in words:
        return 0
    
    queue = deque([(begin, 0)])
    visited = set()
    visited.add(begin)
    
    while queue:
        current_word, steps = queue.popleft()
        
        for word in words:
            if word not in visited and is_transformable(current_word, word):
                if word == target:
                    return steps + 1
                visited.add(word)
                queue.append((word, steps + 1))
    
    return 0
