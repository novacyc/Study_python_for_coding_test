def solution_1(balls):
    result = 0
    for i in range(len(balls)):
        for j in range(i+1, len(balls)):
            if balls[i] != balls[j]:
                result += 1        
    return result
def solution_2(n, m, balls):
    weight = [0] * (m+1)
    for ball in balls:
        weight[ball] += 1
    
    result = 0
    for i in range(1, m+1):
        n -= weight[i]
        result += n * weight[i]
    return result
        
 
if __name__ == "__main__":
    n, m = map(int, input().split())
    balls = list(map(int, input().split()))
    balls.sort()
    
    print(solution_1(balls))
    print(solution_2(n, m, balls))

"""
5 3
1 3 2 3 2
-> 8

8 5
1 5 4 3 2 4 5 2
-> 25
"""
