import random

def RandomSeed():
    random.seed(1)
    for i in range(5):
        print('{:04.3f}'.format(random.random()), end=' ')
    print()

