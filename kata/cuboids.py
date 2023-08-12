# function findDifference(a = [], b = []) {
#     const ca = a.reduce((acc,nxt) => acc * nxt,1);
#     const cb = b.reduce((acc,nxt) => acc * nxt,1);

#     const min = Math.min(ca,cb);
#     const max = Math.max(ca,cb);

#     return max - min;
# }

from functools import reduce

def find_difference(a = [], b = []):
    ca = reduce(lambda acc,curr: acc * curr, a,1)
    cb = reduce(lambda acc,curr: acc * curr, b,1)

    minVal = min(ca,cb)
    maxVal = max(ca,cb)

    return maxVal - minVal