def middle_square(seed=9731, length=1000):
    max_value = 10 ** 10 - 1

    for i in range(length):
        squared = seed ** 2
        digits = str(squared)[len(str(squared)) // 2 - 2: len(str(squared)) // 2 + 2]
        seed = int(digits)

        yield seed / max_value




