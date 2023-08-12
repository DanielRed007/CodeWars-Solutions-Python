from functools import reduce

def sqr_helper(val = 0):
    return pow(val,2)

def square_sum(numbers):
    sqrList = list(map(sqr_helper,numbers))
    
    sum = reduce(lambda acc, curr: acc + curr, sqrList, 0)
    return sum

square_sum([1,2])