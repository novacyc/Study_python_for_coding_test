https://programmers.co.kr/learn/courses/30/lessons/42891
def solution(food_times, k):
    
    allkill = sum(food_times)
    result = 0
    
    while allkill:
        for i,v in enumerate(food_times):
            if k == 0:
                return (i+1)
            if v != 0:
                food_times[i] -= 1
                allkill -= 1
                k -= 1
            else:
                continue
    return -1

print(solution([3,1,2], 5))