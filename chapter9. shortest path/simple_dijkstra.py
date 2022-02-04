def get_near_node():
    index = 0
    min = INF
    for i in range(n+1):
        if distance[i] < min and not visited[i]:
            min = distance[i]
            index = i
    return index

def dijkstra(start):
    distance[start] = 0
    visited[start] = True
    
    for node in graph[start]:
        distance[node[0]] = node[1]
    

    for i in range(n-1):
        next = get_near_node()
        visited[next] = True
        for node in graph[next]:
            tmp = distance[next] + node[1]
            if tmp < distance[node[0]]:
                distance[node[0]] = tmp

if __name__ == '__main__':
    n, m = map(int, input().split())
    start = int(input())

    graph = [[] for _ in range(n+1)]
    visited = [False] * (n+1)
    INF = int(1e9)
    distance = [INF] * (n+1)

    for _ in range(m):
        a, b, c = map(int, input().split())
        graph[a].append((b,c))
    
    dijkstra(start)
    
    for i,v in enumerate(distance):
        print(f"{i} : {v}")
        

"""
6 11
1
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
"""