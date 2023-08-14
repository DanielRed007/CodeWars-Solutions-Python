def duplicate_count(text = ""):
    charSet = list(text.lower())
    count = {}
    result = []

    for char in charSet:
        if char in count:
            count[char] += 1
        else:
            count[char] = 1
    
    for letter in count:
        if count[letter] > 1:
            result.append(letter)
    
    return len(result)

duplicate_count("") # 0)
duplicate_count("abcde") # 0)
duplicate_count("abcdeaa") # 1)
duplicate_count("abcdeaB") # 2)
duplicate_count("Indivisibilities") # 2)