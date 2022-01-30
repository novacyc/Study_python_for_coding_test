def add_max():
    """N:리스트 크기, M:더하기 횟수, K:특정 인덱스 연속 더하기
    """
    N, M, K = map(int, input().split())
    array = list(map(int, input().split()))
    array.sort()
    s, r = divmod(M, K)
    result = array[N-1] * s*K + array[N-2] *r
    return result 
        
if __name__ == '__main__':    
    print(add_max())
     