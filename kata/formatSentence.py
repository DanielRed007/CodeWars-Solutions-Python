

# function formatWords(words = []){
#     let filteredList = words && words.filter(wrd => wrd !== "");
#     let format = ""

#     if(!filteredList || filteredList.length === 0){
#         return "";
#     }
    
#     if(filteredList.length === 1){
#         return filteredList[0];
#     }

#     if(filteredList.length === 2){
#         return filteredList[0] + " and " + filteredList[1];
#     } else {
#         for(let x = 0; x < filteredList.length; x++){
#             if(x === filteredList.length - 1){
#                 format += " and " + filteredList[x];
#             }
            
#             if(x === filteredList.length - 2){
#                 format += filteredList[x];
#             }

#             if(x < filteredList.length - 2){
#                 format += filteredList[x] + ", ";
#             }
#         }
#     }
    
#     return format;
# }

def format_words(words = []):
    pass

format_words(['one', 'two', 'three', 'four']) # 'one, two, three and four', "formatWords(['one', 'two', 'three', 'four'] should return 'one, two, three and four'")
format_words(['one']) # 'one', "formatWords(['one']) should return 'one'")
format_words(['one', '', 'three']), # 'one and three', "formatWords(['one', '', 'three']) should return 'one and three'")
format_words(['', '', 'three']) # 'three', "formatWords(['', '', 'three']) should return 'three'")
format_words(['one', 'two', '']) # 'one and two', "formatWords(['one', 'two', '']) should return 'one and two'")
format_words([]) # '', 'formatWords([]) should return ""')
format_words(None) # '', 'formatWords(null) should return ""')
format_words(['']) # '', 'formatWords([""]) should return ""')