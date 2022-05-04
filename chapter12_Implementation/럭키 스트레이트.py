def solution(value):
    value = list(map(int, str(value)))
    mid = int(len(value) // 2)

    if sum(value[:mid]) == sum(value[mid:]):
        return "LUCKY"
    else:
        return "READY"


print(solution(123402))
print(solution(7755))