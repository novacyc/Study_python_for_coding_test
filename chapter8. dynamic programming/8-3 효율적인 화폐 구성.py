def min_money_greedy():
    n, target = map(int, input().split())
    array = list()
    for _ in range(n):
        array.append(int(input()))
    array.sort(reverse=True)
    
    count = 0
    for i in array:
        s, r = divmod(target, i)
        if s > 0:
            count += s
            target = r
    
    if r != 0:
        return -1
    else:
        return count

def min_money_dynamic():
    n, target = map(int, input().split())
    array = list()
    for _ in range(n):
        array.append(int(input()))
    count = [10001] * (target + 1)
    count[0] = 0
    
    for i in range(n):
        for j in range(array[i], target+1):
            if count[j-array[i]] != 10001:
                count[j] = min(count[j], count[j-array[i]] + 1)
    
    if count[target] == 10001:
        return -1
    else:
        return count[target]
  
print(min_money_greedy())
print(min_money_dynamic())