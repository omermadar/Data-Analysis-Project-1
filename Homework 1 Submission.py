import json
import random
import requests
from math import sqrt


ids = ['212742472', '322793761']


def plus_minus(lst):
    """
    Returns the sum of a list of numbers, with alternating signs.
    First element is with +
    lst: A list of numbers
    """
    # TODOD: Implement this function
    x = 1
    sum = 0
    for item in lst:
        sum += item * x
        x = x * -1
    return sum

def median(lst):
    """
    Returns the median of a list of numbers.
    lst: A list of numbers
    """
    g = sorted(lst)
    size = int(len(g))
    if(int(size) % 2 == 0):
        return (g[int(size / 2 - 1)] + g[int(size / 2)]) / 2
    else:
        return g[int((size - 1) / 2)]
    # TODOD: Implement this function


def std(lst):
    """
    Returns the sample standard deviation of a list of numbers.
    lst: A list of numbers
    """
    # TODOD: Implement this function
    sum = 0
    for item in lst:
        sum += item
    avg = sum / len(lst)
    s = 0
    for item in lst:
        s += (item - avg) ** 2
    s = s / (len(lst) - 1)
    return sqrt(s)
    

def apply_func_shuffle(lst, f1, f2):
    """
    Applies f1 and f2 on a shuffled version of lst (not on lst itself)
    lst: A list of numbers
    Returns two values: the result from f1, and the result from f2    
    """
    shuffled_lst = list(lst)  # do not change
    random.shuffle(shuffled_lst)  # do not change
    # TODO: Implement the rest of this function
    result1 = f1(shuffled_lst)
    result2 = f2(shuffled_lst)
    return result1, result2
    

if __name__ == '__main__':
    # DO NOT CHANGE THE FOLLOWING CODE
    random.seed(sum([int(i) for i in ids]))
    lst = [random.randint(0, 100) for _ in range(100)]
    
    res = {"median": round(median(lst), 3),
           "std": round(std(lst), 3),
           "plus_minus": round(plus_minus(lst), 3),
           "req_ver": requests.__version__,
           }
    med_shuf, plus_minus_shuf = apply_func_shuffle(lst, median, plus_minus)
    res.update({"median_shuffle": round(med_shuf, 3),
                "plus_minus_shuffle": round(plus_minus_shuf, 3)})
    with open("output.json", "w") as f:
        json.dump(res, f)
        
