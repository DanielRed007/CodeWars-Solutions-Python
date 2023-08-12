
def find_outlier(integers):
    
    odd = []
    even = []

    for num in integers:
        
        if (num % 2) == 0:
            even.append(num)
        else:
            odd.append(num)
    
    if(len(odd) == 1):
        return odd[0]
    else:
        return even[0]

find_outlier([2, 4, 6, 8, 10, 3]) #, 3)
find_outlier([2, 4, 0, 100, 4, 11, 2602, 36]) #, 11)
find_outlier([160, 3, 1719, 19, 11, 13, -21]) #, 160)   