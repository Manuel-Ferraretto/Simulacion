def linear_congruential(seed=1234, a=65539, c=0, m=2**31, length=1000):
    max_value = m - 1
    for i in range(length):
        seed = (a * seed + c) % m
        digits = str(seed)[len(str(seed)) // 2 - 2: len(str(seed)) // 2 + 2]
        seed = int(digits)

        yield seed



