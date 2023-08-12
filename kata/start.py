
def even_or_odd(number):
    if number % 2 == 0:
        return 'Even'
    else:
        return 'Odd'
    
def solution(n):
    return sum([x for x in range(n) if x % 3 == 0 or x % 5 == 0])

def getCount(str):
    return len([x for x in str if x in 'aeiou'])

def spin_words(exp):
    s1 = exp.split(" ")
    result = []
    for word in s1:
        if len(word) >= 5:
            result.append(word[::-1])
        else:
            result.append(word)
        
    return " ".join(result)