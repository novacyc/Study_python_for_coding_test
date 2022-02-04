INF = int(1e9)

n = int(input())
m = int(input())

graph = [[INF] * (n+1) for _ in range(n+1)]

for a in range(1, n+1):
    for b in range(1, n+1):
        if a==b:
            graph[a][b] = 0

for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a][b] = c
    
for k in range(1, n+1):
    for i in range(1, n+1):
        for j in range(1, n+1):
            graph[i][j] = min(graph[i][j] , graph[i][k]+ graph[k][j])
            

for a in range(1, n+1):
    for b in range(1, n+1):
        if graph[a][b] == INF:
            print("*", end = "  ")
        else:
            print(graph[a][b], end = "  ")
    print()            
    
"""
6 
11
1 2 2
1 3 5
1 4 1
2 3 3
2 4 2
3 2 3
3 6 5
4 3 3
4 5 1
5 3 1
5 6 2

0 : 1000000000
1 : 0
2 : 2
3 : 3
4 : 1
5 : 2
6 : 4
"""