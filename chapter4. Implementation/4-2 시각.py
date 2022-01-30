def time_in_three():
    """ n_solution : '3' in str(h) + str(m) + str(s)
    """

    n = int(input())
    hours = [i for i in range(n+1)]
    minutes = [i for i in range(60)]
    seconds = minutes[:]
    count = 0
    
    for h in hours:
        if '3' in str(h):
            count += len(minutes) * len(seconds)
            continue
        for m in minutes:
            if '3' in str(m):
                count += len(seconds)
                continue
            for s in seconds:
                if '3' in str(s):
                    count +=1
                
    return count
    
if __name__ == "__main__":
    print(time_in_three())
    
""" 
5
---------
11475
"""