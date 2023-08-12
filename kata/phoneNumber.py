
def create_phone_number(numbers = []):
    chars = "".join(numbers)

    sec1 = chars[0:3]
    sec2 = chars[3:6]
    sec3 = chars[6:10]

    return f"(${sec1}) ${sec2}-${sec3}"