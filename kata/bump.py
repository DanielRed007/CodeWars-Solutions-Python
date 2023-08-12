

def bump_filter(char):
    return char != "_"

def bumps(road = ""):
    roadF = [char for char in road]
    filteredList = filter(bump_filter,roadF)
    char_set = list(filteredList)
    
    if(len(char_set) <= 15):
        return "Woohoo!"
    else:
        return "Car Dead"

bumps("n") # "Woohoo!")
bumps("__nn_nnnn__n_n___n____nn__nnn") # "Woohoo!")
bumps("nnn_n__n_n___nnnnn___n__nnn__") # "Woohoo!")
bumps("_nnnnnnn_n__n______nn__nn_nnn") # "Car Dead")
bumps("______n___n_") # "Woohoo!")
bumps("nnnnnnnnnnnnnnnnnnnnn") # "Car Dead")