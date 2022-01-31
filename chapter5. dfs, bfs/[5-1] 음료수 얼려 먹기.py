def icecream(x, y):
    if x not in range(H) or y not in range(W):
        return False
    
    if graph[x][y] == 0:
        graph[x][y] = 1
        icecream(x-1, y)
        icecream(x+1, y)
        icecream(x, y+1)
        icecream(x, y-1)
        return True
    else:
        return False

if __name__ == "__main__":
    H, W = map(int, input().split())   
    graph=list()
    for _ in range(H):
        graph.append(list(map(int, input().split())))
        
    cnt = 0
    for x in range(H):
        for y in range(W):
            if icecream(x, y) == True:
                cnt += 1
    print(cnt)  
    
"""
3 3
0 0 1
0 1 0
1 0 1
----------
3
"""