def mean_opredelyator(*args):
    s = 0
    for arg in args:
        s += arg
    
    return s / len(args)


mean = mean_opredelyator(1, 1, 1, 5, 4, 3)
print(mean)


def mean_opredelyator(*args):
    return sum(args) / len(args)


mean = mean_opredelyator(1, 1, 1, 5, 4, 3)
print(mean)