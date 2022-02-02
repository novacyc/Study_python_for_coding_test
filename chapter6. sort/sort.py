def select_sort(obj):
    n = len(obj)
    
    for i in range(n):
        min_idx = i
        for j in range(i, n):
            if obj[min_idx] > obj[j] :
                min_idx = j
        obj[min_idx], obj[i] = obj[i], obj[min_idx]
                
    return obj
def insert_sort(obj):
    n = len(obj)
    
    for i in range(1, n):
        for j in range(i, 0, -1):
            if obj[j] < obj[j-1]:
                obj[j], obj[j-1] = obj[j-1], obj[j]
            else:
                break
    return obj
def quick_sort(obj):
    if len(obj) <= 1:
        return obj
    
    pivot = obj[0]
    tail = obj[1:]
    
    left_side = [x for x in tail if x <= pivot]
    right_side = [x for x in tail if x > pivot]
    
    return quick_sort(left_side) + [pivot] + quick_sort(right_side)    
def counting_sort(obj):
    count = [0] * (max(obj) + 1)
    
    for i in range(len(obj)):
        count[obj[i]] += 1
        
    for i in range(len(count)):
        for j in range(count[i]):
            print(i, end=' ')

    
if __name__ == '__main__':
    obj = [7,5,9,0,3,1,6,2,4,8]
    print("select : ", select_sort(obj))
    print("insert : ", insert_sort(obj))
    print("quick : ", quick_sort(obj))
    print("count : ", end ='')
    counting_sort(obj)
