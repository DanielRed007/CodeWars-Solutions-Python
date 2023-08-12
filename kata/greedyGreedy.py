def score(dice = []):
    data = {}

    for num in dice:

        strNum = str(num)
        if strNum in data:
            data[strNum] += 1
        else:
            data[strNum] = 1

    triples = 0
    finalScore = 0

    for set in data:

        if data[set] >= 3:
            triples = int(set)
            data[set] = (data[set] - 3)
        
    
    if triples != 0:
        if triples == 1:
            finalScore += 1000
        else:
            finalScore += triples * 100


    for remain in data:
        if int(remain) == 1:
            finalScore += (int(data[remain]) * 100)
        
        if int(remain) == 5:
            finalScore += (int(data[remain]) * 50)

    return finalScore
    

score([5, 1, 3, 4, 1]) #  250)
score([1, 1, 1, 3, 1]) # 1100)
score([2, 3, 4, 6, 2]) #    0)
score([4, 4, 4, 3, 3]) #  400)
score([2, 4, 4, 5, 4]) #  450)