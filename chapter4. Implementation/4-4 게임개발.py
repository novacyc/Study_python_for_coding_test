def turn_left(d):
    #N, W, S, E
    order = [0, 3, 2, 1]
    next_d = order[(order[d] + 1) % 4]
    return next_d

def game():
    """
    (0,0) ~ (n-1, n-1)
    회전순서  W -> S -> E -> N
    방향 0 : N, 1: E, 2: S, 3 : W
    육지, 바다 0: earth, 1: sea , 2: 방문한 곳
    """
    N,M = map(int, input().split())
    x,y,d = map(int, input().split())
    inf = list()
    for _ in range(N):
        inf.append(list(map(int, input().split())))
    count = 1
    
    #N, E, S, W
    dx = [-1, 0, 1, 0]
    dy = [0, 1, 0, -1]
    count_rotation = 0
    
    print()
    while True:
        d = turn_left(d)
        next_x = x + dx[d]
        next_y = y + dy[d]   
        print(next_x, next_y, d, count_rotation, end="->")

        if inf[next_x][next_y] == 0:
            count_rotation =0
            count += 1
            inf[x][y] = 2
            x, y = next_x, next_y
            print()
            print(f"next : {x}, {y}, {d}, {count_rotation}")
            print()
        else:
            count_rotation += 1
            if count_rotation == 4:
                d = turn_left(d)
                next_x = x + dx[d]
                next_y = y + dy[d]  
                #뒤가 바다면, 끝
                if inf[next_x][next_y] == 1:
                    print()
                    break;
                else:
                    x,y = next_x, next_y

    return count    

if __name__ == "__main__":
    print(game())
"""
4 4
1 1 0
1 1 1 1
1 0 0 1
1 1 0 1
1 1 1 1
------------------
3
(1,1,0) -> (1,1,)
"""