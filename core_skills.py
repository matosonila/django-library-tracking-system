import random
rand_list = random.randint(1,20)

list_comprehension_below_10 = [num for num in rand_list if num <= 10]

def func_filter(x):
    return x <= 10

list_comprehension_below_10 = [func_filter(num) for num in rand_list]