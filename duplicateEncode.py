def duplicate_encode(word = ""):
    lower = word.lower()
    count = {}
    result = ""

    for char in lower:
        if char in count:
            count[char] += 1
        else:
            count[char] = 1

    for char in lower:
        if count[char] == 1:
            result += "("
        else:
            result += ")"

    return result

duplicate_encode("din") #"(((")
duplicate_encode("recede") #"()()()")
duplicate_encode("Success") #")())())","should ignore case")
duplicate_encode("(( @") #"))((")