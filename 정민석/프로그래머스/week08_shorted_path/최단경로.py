import heapq
import sys

input = sys.stdin.read
INF = float('inf')

def dijkstra(V, adj, start):
    dist = [INF] * (V + 1)
    dist[start] = 0
    min_heap = [(0, start)] 
    
    while min_heap:
        current_dist, u = heapq.heappop(min_heap)
        
        if current_dist > dist[u]:
            continue
        
        for weight, v in adj[u]:
            distance = current_dist + weight
            if distance < dist[v]:
                dist[v] = distance
                heapq.heappush(min_heap, (distance, v))
    
    return dist

input_data = input().split()
idx = 0
V = int(input_data[idx])
E = int(input_data[idx + 1])
idx += 2
start = int(input_data[idx])
idx += 1

adj = [[] for _ in range(V + 1)]

for _ in range(E):
    u = int(input_data[idx])
    v = int(input_data[idx + 1])
    w = int(input_data[idx + 2])
    adj[u].append((w, v))
    idx += 3

dist = dijkstra(V, adj, start)

for i in range(1, V + 1):
    if dist[i] == INF:
        print("INF")
    else:
        print(dist[i])