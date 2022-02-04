#A -> K -> X
import sys
def future_city():
    input = sys.stdin.readline
    n, m = map(int, input().split())
    INF = int(1e9)
    graph = [[INF] * (n+1) for _ in range(n+1)]
    
    for a in range(1, n+1):
        for b in range(1, n+1):
            if a==b:
                graph[a][b] = 0
                
    for _ in range(m):
        a, b = map(int, input().split())
        graph[a][b] = 1
        graph[b][a] = 1
        

    x, k = map(int, input().split())
    
    for c in range(1, n+1):
        for a in range(1, n+1):
            for b in range(1, n+1):
                 graph[a][b] = min(graph[a][b], graph[a][c] + graph[c][b])

    return (graph[1][k] + graph[k][x])

if __name__ == "__main__":
    print(future_city())
    
    
"""
5 7
1 2
1 3
1 4
2 4
3 4
3 5
4 5
4 5

4 2
1 3
2 4
3 4
"""