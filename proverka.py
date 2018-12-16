def sum (zzz, ddd):
    """What percentage of x is y"""
    result = zzz+ddd
    #print("first sum of " + str(zzz) + " and " + str(ddd) + " is " + str (result))
    return result


def print_sum(x, y):
    """Print what percentage of x is y"""
    print("second sum of " + str(x) + " and " + str(y) + " is " + str(sum (x, y)))


print_sum(3,20)