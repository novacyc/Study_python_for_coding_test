from audioop import reverse


def reverse_sorrt():
    n = int(input())
    array = []
    for _ in range(n):
        array.append(int(input()))
    
    array.sort(reverse=True)
    print(array)
    
    

if __name__ == '__main__':
    reverse_sorrt()

"""
3
15
27
12
"""