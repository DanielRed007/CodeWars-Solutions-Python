def get_squares(number=0):
    digits = [int(digit) for digit in str(number)]
    squares = [digit ** 2 for digit in digits]
    sum_of_squares = sum(squares)

    return sum_of_squares

def is_happy(n):
    
    tracker = []

    while n > 0:
        n = get_squares(n)
        tracker.append(n)

        if n == 1:
            return True
        
        dList = [i for i in tracker if tracker.count(i) > 1]

        if len(dList) == 2:
            return False