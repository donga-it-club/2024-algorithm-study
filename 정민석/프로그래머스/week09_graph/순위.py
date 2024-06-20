def solution(n, results):
    INF = float('inf')
    
    # 승패를 나타내는 2차원 배열 생성 (자기 자신으로 가는 경로는 0으로 초기화)
    graph = [[INF] * (n + 1) for _ in range(n + 1)]
    for i in range(1, n + 1):
        graph[i][i] = 0
    
    # 결과를 바탕으로 그래프 초기화
    for winner, loser in results:
        graph[winner][loser] = 1
    
    # 플로이드-워셜 알고리즘 적용
    for k in range(1, n + 1):
        for i in range(1, n + 1):
            for j in range(1, n + 1):
                if graph[i][j] > graph[i][k] + graph[k][j]:
                    graph[i][j] = graph[i][k] + graph[k][j]
    
    answer = 0
    
    # 각 선수에 대해 승패가 확실한 선수의 수를 세기
    for i in range(1, n + 1):
        count = 0
        for j in range(1, n + 1):
            if graph[i][j] != INF or graph[j][i] != INF:
                count += 1
        # 자기 자신을 제외하고 모든 선수와의 승패 관계가 확실하면 순위를 매길 수 있음
        if count == n:
            answer += 1
    
    return answer
