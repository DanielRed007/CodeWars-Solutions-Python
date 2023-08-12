def char_counter(text = ""):
    counter = {}

    for char in text:
        if char in counter:
            counter[char] += 1
        else:
            counter[char] = 1
    
    return counter

def added_char(s1 = "", s2 = ""):
    counter1 = char_counter(s1)
    counter2 = char_counter(s2)

    for data in counter2:
        if counter2[data] == counter1.get(data, 0):
            counter2[data] = 0

    maxChar = max(counter2.values())
    result = [key for key, value in counter2.items() if value == maxChar]

    return result[0]

added_char("hello","checlclo")