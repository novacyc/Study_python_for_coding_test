def card_game():
    M, N = map(int, input().split())
    result = 0
      
    for _ in range(M):
        line = list(map(int, input().split()))
        min_v = min(line)
        result = max(min_v, result)

    return result

if __name__ == '__main__':
    print(card_game())


"""
3 3
3 1 2
4 1 4

2 4
7 3 1 8
3 3 3 4
"""