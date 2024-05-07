def solution(s):
    a = 0
    for i in s:
        if a < 0:
            break
        a = a + 1 if i == "(" else a - 1
    return a == 0