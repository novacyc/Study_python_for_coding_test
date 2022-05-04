def solution(value):
    value = sorted(list(value))
    numeric = [str(i) for i in range(1, 10)]
    
    sum = 0
    for v in value[:]:
        if v in numeric:
            sum += int(v)
            value.remove(v)
            
    value.append(str(sum))
    return "".join(value)
         
    
    
print(solution("K1KA5CB7"))
print(solution("AJKDLSI412K4JSJ9D"))