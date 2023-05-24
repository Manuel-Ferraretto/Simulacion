import random
import secrets


def random_function(a, limit):
    if a is None:
        random.seed()
    elif a >= 0:
        random.seed(a, version=2)

    count = 0
    results = []
    while count < limit:
        #yield random.random()
        results.append(random.random())
        count += 1

    return results


def secrets_function(limit, bits=64):
    max_value = 2 ** bits
    count = 0
    results = []
    while count < limit:
        count += 1
        #yield secrets.randbits(bits) / max_value
        results.append(secrets.randbits(bits) / max_value)

    return results




'''
print(random_function(None, 50))
print(secrets_function(10))

rand = random_function(None, 50)
for i in range(50):
    print(next(rand))
'''