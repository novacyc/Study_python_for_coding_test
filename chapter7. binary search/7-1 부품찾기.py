def binary_search(array, target, start, end):
    if start > end:
        return None
    mid = (start+end) // 2
    
    if array[mid] == target:
        return mid
    elif array[mid] > target:
        return binary_search(array, target, mid+1, end)
    else:
        return binary_search(array, target, start, mid-1)

def search_part():
    n = int(input())
    parts = list(map(int, input().split()))
    
    m = int(input())
    search_parts = list(map(int, input().split()))
    
    for part in search_parts:
        result = binary_search(parts, part, 0, len(parts) - 1)
        if result != None:
            print(f"{part} : yes")
        else:
            print("%d : no" %part)
if __name__=="__main__":
    search_part()

"""
5
8 3 7 9 2
3
5 7 9
"""