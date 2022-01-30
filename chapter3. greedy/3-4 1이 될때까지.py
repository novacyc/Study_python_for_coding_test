def to_one():
    """1 or 2
    1. N-1
    2. N/k (단, 나누어떨어질때만)
    """
    N, K = map(int, input().split())
    count = 0
    
    while N > 1:
        if N % K == 0:
            N /= K
        else:
            N -=1
        count +=1
    return count    

if __name__ == '__main__':
    print(to_one())
    
"""""
in:
25 5
out:
2
"""""