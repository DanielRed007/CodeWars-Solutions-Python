
# function sortTheInnerContent(words = ""){
#     return words.split(" ").map(word => {
#         const inner = word.slice(1,word.length - 1).split("").sort((a,b) => b.localeCompare(a)).join("");
#         return word.length > 3 ? word[0] + inner + word[word.length - 1] : word;
#     }).join(" ");
# };

def sort_helper(wrd = ""):
  inner = list(wrd)[1:len(wrd) - 1]
  inner.sort(reverse=True)
  
  if len(wrd) > 3:
    return wrd[0] + "".join(inner) + wrd[len(wrd) - 1]
  else:
    return wrd

def sort_the_inner_content(words = ""):
  wordList = words.split(" ")
  sorted = list(map(sort_helper,wordList))
  
  return " ".join(sorted)

print(sort_the_inner_content("sort the inner content in descending order")) #  "srot the inner ctonnet in dsnnieedcg oredr"