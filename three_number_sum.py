#Given an array of integers and a value, 
# determine if there are any three integers in the array whose sum equals the given value.

from itertools import combinations 
import numpy as np

def three_number_sum(arr, val):
    lst=list(combinations(arr, 3))
    print(np.sum(lst, axis=1))
    return any([elm==val for elm in np.sum(lst, axis=1)])

print(three_number_sum([34,5,5,7], 17))