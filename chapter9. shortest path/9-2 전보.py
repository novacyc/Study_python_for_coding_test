#단방향
import sys
import heapq
input = sys.stdin.readline

def floid():
    n, m, c = map(int, input().split())
    
    INF = int(1e9)

    graph = [ [INF] * (n+1) for _ in range(n+1) ]
    
    for a in range(1, n+1):
        for b in range(1, n+1):
            if a==b: graph[a][b] = 0 
    
    for _ in range(m):
        x, y ,z = map(int,input().split())
        graph[x][y] = z
    
    for x in range(1, n+1):
        for y in range(1, n+1):
            for z in range(1, n+1):
                graph[y][z] = min(graph[y][z], graph[y][x] + graph[x][z])

    count, time = 0, 0
    for j in range(2, n+1):
        if graph[1][j] != INF:
            count += 1
            time = max(time, graph[1][j])

    return (count, time)    

if __name__ == "__main__":
    print(floid())
    
"""
3 2 1
1 2 4
1 3 2
"""
    