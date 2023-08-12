# function divisors(int) {
#   let result = [];
#   for(let j = 2; j < int; j++){
#     if(int % j == 0) result.push(j);  
#   }
#   return result.length === 0 ? int + ' is prime' : result;
# };

def divisors(integer):
    result = []

    for num in range(2,integer):
        if integer % num == 0:
            result.append(num)
    
    if len(result) == 0:
        return integer + ' is prime'
    else:
        return result

divisors(12)
divisors(25)
divisors(13)