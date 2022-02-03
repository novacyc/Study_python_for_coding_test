def binary_search(array, target, start, end):
    while start <= end:
        mid = (start + end) // 2
        sum = 0
        for i in array:
            if i > mid:
                sum += (i - mid)
        print(start, mid, end, sum)
        if sum == target:
            return mid
        elif sum > target:
            start = mid + 1
        else:
            end = mid -1
    return None


def make_dduk():
    n, target = map(int, input().split())
    array = list(map(int, input().split()))
    array.sort()
    
    start = array[0]
    end = array[len(array)-1]
    print(binary_search(array,target, start, end))
    
if __name__ == "__main__":
    make_dduk()
    
"""
4 6
17 10 19 15
------------
15
"""