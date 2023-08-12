import functools

# function findOdd(numbers) {

#   let matrix = {};
  
#   numbers.forEach(num => {
#     if(matrix[num] > 0){
#       matrix[num]++
#     } else {
#       matrix[num] = 1
#     }
#   });
  
#   for(let num in matrix){
#     if(matrix[num] % 2){
#       return Number(num);
#     }
#   };
# };

def find_it(seq):
    map = {}

    for val in seq:
        if val in map:
            map[val] += 1
        else:
            map[val] = 1
    
    for val in map:
        if map[val] % 2:
            return int(val)

find_it([1,2,2,3,3,3,4,3,3,3,2,2,1])

# function digital_root(n) {
#   let res = n;
#   while(res > 9){
#     let arr = res.toString().split('')
#       .map(x => parseInt(x))
#       .reduce((a,b) => a + b);
#     res = arr;
#   }
#   return res;
# }

def digital_root(n):
    res = n

    while res > 9:
        list1 = list(str(res))
        list1F = list(map(lambda num: int(num), list1))
        redList = functools.reduce(lambda acc, curr: acc + curr, list1F, 0)
        res = redList
    
    return res

digital_root(132189)
