from collections import defaultdict

def dfs(graph, airport, route):
    while graph[airport]:
        next_airport = graph[airport].pop(0)
        dfs(graph, next_airport, route)
        
        
    route.append(airport)

def solution(tickets):
    # 빈 리스트 생성
    # https://stackoverflow.com/questions/19629682/ordereddict-vs-defaultdict-vs-dict
    graph = defaultdict(list)
    
    # 그래프를 생성 -> 티켓을 사전순으로 정렬
    for a, b in sorted(tickets):
        graph[a].append(b)

    route = []

    dfs(graph, "ICN", route)
    
    # 경로가 역순으로 저장되기에 역순으로 반환
    return route[::-1]
