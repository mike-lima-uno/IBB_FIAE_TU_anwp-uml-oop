lambda x: x % 2 == 0

def kafn(x):
    return x % 2 == 0

a=[1,2,3,4]
g1 = list(filter(lambda x: x%2 == 0, a))

g2 = list(filter(kafn, a))