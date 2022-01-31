def factorial_iterative(n : int):
    sum  = 1
    for i in range(1,n+1):
        sum *= i
    return sum
    
def factorial_recurcive(n : int):
    if n <= 1:
        return 1
    else:
        return n*factorial_recurcive(n-1)

print('반복 : ', factorial_iterative(5))
print('재귀 : ', factorial_recurcive(5))