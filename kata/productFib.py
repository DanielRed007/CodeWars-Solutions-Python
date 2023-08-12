import functools

def getFibonacciValue(seq = []):
    fibo = seq[-2:]
    return functools.reduce(lambda a,b: a + b,fibo)

def productFib(product = 0):
    fibonacci = [0,1]
    fibProduct = 0
    result = []
    next = 0

    while fibProduct <= product:
        fibNums = fibonacci[-2:]
        next = getFibonacciValue(fibonacci)
        fibonacci.append(next)
        fibProduct = fibNums[0] * fibNums[1]

        if fibProduct > product:
            fibonacci.pop()
            fibonacci = fibonacci[-2]
            result = [fibNums[0],fibNums[1],False]
            break

        if fibProduct == product:
            result = [fibNums[0],fibNums[1],True]
            break

    return result

productFib(4895) # [55, 89, True]
productFib(5895) # [89, 144, False] 