def solution(triangle):
    # 삼각형의 높이
    n = len(triangle)
    
    # dp 테이블 초기화
    dp = [[0] * n for _ in range(n)]
    
    # 꼭대기 값 초기화
    dp[0][0] = triangle[0][0]
    
    # 동적 프로그래밍을 이용하여 테이블 채우기
    for i in range(1, n):
        for j in range(i + 1):
            if j == 0:
                # 왼쪽 끝인 경우
                dp[i][j] = dp[i - 1][j] + triangle[i][j]
            elif j == i:
                # 오른쪽 끝인 경우
                dp[i][j] = dp[i - 1][j - 1] + triangle[i][j]
            else:
                # 가운데인 경우
                dp[i][j] = max(dp[i - 1][j - 1], dp[i - 1][j]) + triangle[i][j]
    
    return max(dp[-1])


