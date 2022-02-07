def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

def team_union(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    
    if a > b:
        parent[a] = b
    else:
        parent[b] =a
    
def team_check(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    
    if a == b:
        print("YES")
    else:
        print("NO")
    
if __name__ == "__main__":
    n, m = map(int, input().split())
    parent = [0] * (n+1)
    for i in range(n+1):
        parent[i] = i
          
    for _ in range(m):
        p, a, b = map(int, input().split())
        if p == 0:
            team_union(parent, a, b)
        else:
            team_check(parent, a, b)
        
"""
7 8
0 1 3
1 1 7
0 7 6
1 7 1
0 3 7
0 4 2
0 1 1
1 1 1
"""