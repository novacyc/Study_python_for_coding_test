def loser():
    n = int(input())
    array = list()
    for _ in range(n):
        array.append(list(input().split()))
    
    array = sorted(array, key=lambda x:int(x[1]))

    for v in array:
        print(v[0])
    
if __name__ == "__main__":
    loser()
    
"""
3
홍길동 95
이순신 77
장보리 100
"""