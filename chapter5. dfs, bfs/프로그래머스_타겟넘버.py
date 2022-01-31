from collections import deque
def solution(numbers, target):
    answer = 0
    end = len(numbers) - 1
    
    queue = deque()
    queue.append( (0, numbers[0]) )
    queue.append( (0, numbers[0] * -1) )
     
    while queue:
        i, v = queue.popleft()   
        if i == end and v == target:
            answer += 1
        
        if i < end:
            i += 1
            queue.append( (i, v + numbers[i]) )
            queue.append( (i, v - numbers[i]) )
    
    return answer


print(solution([1, 1, 1, 1, 1], 3)) #5
print(solution([4, 1, 2, 1], 4)) #2