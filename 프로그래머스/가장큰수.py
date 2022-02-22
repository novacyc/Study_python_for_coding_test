def solution(numbers):
    numbers = list(map(str, numbers))
    numbers = sorted(numbers, key=lambda x:x+( (4-len(x)) * '0'), reverse=True )
    #numbers = sorted(numbers, key=lambda x:x[0], reverse=True)

    return "".join(numbers)