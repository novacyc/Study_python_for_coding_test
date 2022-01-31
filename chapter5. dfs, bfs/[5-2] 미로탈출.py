from collections import deque


def maze():
    H, W = map(int, input().split())
    info = list()
    for _ in range(H):
        info.append(list(map(int, input())))


    print(info)
    queue = deque()
    queue.append((0, 0))
    # s, n , e, w
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx not in range(H) or ny not in range(W):
                continue
            if info[nx][ny] == 0:
                continue
            if info[nx][ny] == 1:
                info[nx][ny] = info[x][y] + 1
                queue.append((nx, ny))

    return info[H-1][W-1]


if __name__ == "__main__":
    print(maze())

"""
5 6
101010
111111
000001
111111
111111

---------
10
"""
