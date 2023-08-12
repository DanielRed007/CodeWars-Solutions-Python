
# function disemvowel(str) {
#   let result = "";
  
#   for(let x = 0; x < str.length; x++){
    
#     if(/^[aeiou]$/.test(str[x].toLowerCase())){
#       result += "";
#     } else {
#       result += str[x];
#     }
    
#   }
  
#   return result;
# }

import re

def disemvowel(text):
    result = ""

    for letter in text:
        if re.match(r"(?i)^[aeiou]$",letter):
            result += ""
        else:
            result += letter 

    return result