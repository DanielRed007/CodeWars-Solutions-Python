from functools import reduce

def narcissistic(value = 0):
    if value > 0 and value < 10:
        return True
    
    strVals = list(str(value))
    power = len(strVals)

    powList = [pow(int(val),power) for val in strVals]
    reduxVals = reduce(lambda x, y: x + y, powList)

    return reduxVals == value

narcissistic(7) # True, '7 is narcissistic');
narcissistic(371)  # True, '371 is narcissistic');