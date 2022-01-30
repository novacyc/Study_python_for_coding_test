def knight():
    cur_pos = str(input())
    
    x = int(ord(cur_pos[0]) - ord('a')) + 1
    y = int(cur_pos[1])
    steps = [(2,1), (2,-1), (-2,1), (-2,-1), (1,2), (1,-2), (-1,2), (-1,-2)]
    result =0
    
    for step in steps:
        next_x = x+step[0]
        next_y = y+step[1]
        
        if next_x >=1 and next_x <= 8 and next_y >=1 and next_y <=8:
            result +=1

    return result

if __name__ == '__main__':
    print(knight())


"""
c2 -> 6
a1 -> 2
"""