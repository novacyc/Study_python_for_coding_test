def max_change():
    n, c = map(int,input().split())
    
    ori_array = list(map(int, input().split()))
    cha_array = list(map(int, input().split()))
    
    ori_array.sort()
    cha_array = sorted(cha_array, reverse=True)
    
    for i in range(c):
        if ori_array[i] < cha_array[i]:
            ori_array[i], cha_array[i] = cha_array[i], ori_array[i]
        
    return sum(ori_array)
    

if __name__ == "__main__":
    print(max_change())
    
"""
5 3
1 2 5 4 3
5 5 6 6 5
---------------
26
"""