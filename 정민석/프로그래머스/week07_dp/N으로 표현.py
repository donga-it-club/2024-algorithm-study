def solution(N, number):
    if N == number:
        return 1

    #DP 리스트 초기화 (각 인덱스는 N을 사용한 횟수, 각 요소는 N을 사용해 만들 수 있는 숫자들의 집합)
    dp = [set() for _ in range(9)]
    dp[1].add(N)

    # N을 여러 번 사용한 숫자들을 계산
    for i in range(2, 9):
        dp[i].add(int(str(N) * i))  
        for j in range(1, i):
            for x in dp[j]:
                for y in dp[i-j]:
                    dp[i].add(x + y)
                    dp[i].add(x - y)
                    dp[i].add(x * y)
                    if y != 0:
                        dp[i].add(x // y)

        # 매 반복 시 number가 생성되었는지 확인
        if number in dp[i]:
            return i

    return -1
