# function to_nato(words = "") {
#     const formatWords = words.toLowerCase();

#     let cipher = "";
#     const specialChars = [",",".","!","?"];

#     for(let x = 0; x < formatWords.length; x++){
#         const char = formatWords[x];

#         if(Object.keys(NATO).some(nato => char === nato)){
#             cipher += NATO[char] + " ";
#         }

#         if(specialChars.some(spec => char === spec)){
#             cipher += char + " ";
#         }
#     }

#     return cipher.trim();
# }

import string

NATO = {'A': 'Alfa', 'B': 'Bravo', 'C': 'Charlie', 'D': 'Delta', 'E': 'Echo', 'F': 'Foxtrot', 'G': 'Golf', 'H': 'Hotel', 'I': 'India', 'J': 'Juliett', 'K': 'Kilo', 'L': 'Lima', 'M': 'Mike', 'N': 'November', 'O': 'Oscar', 'P': 'Papa', 'Q': 'Quebec', 'R': 'Romeo', 'S': 'Sierra', 'T': 'Tango', 'U': 'Uniform', 'V': 'Victor', 'W': 'Whiskey', 'X': 'Xray', 'Y': 'Yankee', 'Z': 'Zulu'}

def to_nato(words = ""):
    formatWords = words.upper()

    nato = ""

    for char in formatWords:
        
        if char in NATO.keys():
            nato += NATO[char] + " "
        
        if char in string.punctuation:
            nato += char + " "
    
    return nato.strip()


to_nato('If you can read') # "India Foxtrot Yankee Oscar Uniform Charlie Alfa November Romeo Echo Alfa Delta"
to_nato('If, you can read?') # "India Foxtrot , Yankee Oscar Uniform Charlie Alfa November Romeo Echo Alfa Delta ?"