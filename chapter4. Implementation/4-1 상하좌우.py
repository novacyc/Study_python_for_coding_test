def lrud():
    """logic : [좌표 이동에 대해 dict, 좌표 (1,1) ~ (n,n)을 벗어나지 않는 범위에서 연산 수행 후 return]
        d_logic : [dx, dy, move_types에 대해 각각 리스트, 리스트 index 활용]
    """
    n = int(input())
    plans = list(map(str, input().split()))
    locs = { 
            'R' : [0, 1],
            'L' : [0, -1],
            'U' : [-1, 0],
            'D' : [1, 0]
            }
    
    x, y= 1, 1
    
    for plan in plans:
        next_x = x + locs[plan][0]
        next_y = y + locs[plan][1]
        
        if next_x in range(1,n+1) and next_y in (range(1, n+1)):
            x, y = next_x, next_y
        else:
            continue
    return x, y

if __name__ == "__main__":
    print(lrud())


"""
5
R R R U D D
---------
3 4
"""