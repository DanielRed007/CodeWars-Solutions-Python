
# function consonantCount(text = ""){
#     const consonants = [
#         'b', 'c', 'd', 'f', 'g',
#         'h', 'j', 'k', 'l', 'm',
#         'n', 'p', 'q', 'r', 's',
#         't', 'v', 'w', 'x', 'y',
#         'z'
#     ];

#     return text.split("").filter(char => consonants.some(con => char.toLowerCase() ===  con)).length;
# }

def consonant_count(text):
    consonants = [
        'b', 'c', 'd', 'f', 'g',
        'h', 'j', 'k', 'l', 'm',
        'n', 'p', 'q', 'r', 's',
        't', 'v', 'w', 'x', 'y',
        'z'
    ]

    count = 0

    for char in text:
        if char.lower() in consonants:
            count += 1

    return count