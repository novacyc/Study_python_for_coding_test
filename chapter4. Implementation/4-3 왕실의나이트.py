def knight():
    cur_pos = str(input())
    
    x = int(ord(cur_pos[0]) - ord('a')) + 1
    y = int(cur_pos[1])
    all_pos = [(x,y) for x in range(1,9) for y in range(1,9)]
    possible_pos = [(x+2, y+1),(x+2, y-1), (x-2, y+1), (x-2, y-1), (x+1, y+2), (x+1, y-2), (x-1, y+2), (x+1, y-2)]
    count = 0
    
    for pos in all_pos:
        if pos in possible_pos:
            count += 1
    return count

if __name__ == '__main__':
    print(knight())


"""
c2 -> 6
a1 -> 2
"""