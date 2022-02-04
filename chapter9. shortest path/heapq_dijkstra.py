import heapq
import sys

input = sys.stdin.readline

n, m = map(int, input().split())
start = int(input())
graph = [[] for i in range(n+1)]
INF = int(1e9)
distance = [INF] * (n+1)


for _ in range(m):
    a,b,c = map(int, input().split())
    graph[a].append((b,c))
    
def dijkstra(start):
    q = []
    heapq.heappush(q, (0, start))
    distance[start] = 0
    
    while q:
        dis, now = heapq.heappop(q)
        
        if dis > distance[now] :
            continue
        
        for next in graph[now]:
            cost = dis + next[1]
            if cost < distance[next[0]]:
                distance[next[0]] = cost
                heapq.heappush(q, (cost, next[0]))
                
dijkstra(start)

for i in distance:
    print(i)