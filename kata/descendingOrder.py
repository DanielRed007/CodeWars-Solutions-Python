
# function accum(string) {
#   let toLower =string.toLowerCase();
#   let newString = '';
# 	for(let x = 0; x < toLower.length; x++){
#         let addString = toLower[x];
#         if(x == 0){
#             newString += `${addString.toUpperCase()}`;
#         } else {
#             newString += `-${addString.toUpperCase()}`;            
#             for(let y = 0; y < x; y++){                
#                 newString += addString;
#             }
#         }
#     }
#     return newString;
# }

def accum(text):
    lower = text.lower()
    accum = ""

    for index, val in enumerate(lower):
        if index == 0:
            accum += val.upper()
        else:
            accum += "-" + val.upper()
            for x in range(0,index):
                accum += val

    return accum

accum("ZpglnRxqenU") # "Z-Pp-Ggg-Llll-Nnnnn-Rrrrrr-Xxxxxxx-Qqqqqqqq-Eeeeeeeee-Nnnnnnnnnn-Uuuuuuuuuuu"
# accum("NyffsGeyylB") # "N-Yy-Fff-Ffff-Sssss-Gggggg-Eeeeeee-Yyyyyyyy-Yyyyyyyyy-Llllllllll-Bbbbbbbbbbb"
# accum("MjtkuBovqrU") # "M-Jj-Ttt-Kkkk-Uuuuu-Bbbbbb-Ooooooo-Vvvvvvvv-Qqqqqqqqq-Rrrrrrrrrr-Uuuuuuuuuuu"
# accum("EvidjUnokmM") # "E-Vv-Iii-Dddd-Jjjjj-Uuuuuu-Nnnnnnn-Oooooooo-Kkkkkkkkk-Mmmmmmmmmm-Mmmmmmmmmmm"
# accum("HbideVbxncC") # "H-Bb-Iii-Dddd-Eeeee-Vvvvvv-Bbbbbbb-Xxxxxxxx-Nnnnnnnnn-Cccccccccc-Ccccccccccc"