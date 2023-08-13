# function cubeOdd(list = []) {
#     return list.some(val => !Number.isInteger(val)) ? undefined : 
#     list.map(num => Math.pow(num,3)).filter(num => num % 2).reduce((acc,nxt) => acc + nxt, 0)
# }

import math

def cube_values(num):
    return math.floor(math.pow(num,3))

def is_even(num):
    return  num % 2

def cube_odd(numberSet = []):
    result = 0

    for val in numberSet:
        if not isinstance(val, (int,float)):
            return None
        if isinstance(val, (bool)):
            return None
    
    cubed = list(filter(is_even,list(map(cube_values,numberSet))))
    
    for val in cubed:
        result += val

    return result

cube_odd([1, 2, 3, 4]) # 28)
cube_odd([-3,-2,2,3]) # 0)
cube_odd(["a",12,9,"z",42]) # None)
cube_odd([True, False, 2, 4, 1]) # None