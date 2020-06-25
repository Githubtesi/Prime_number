# Input
# [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]

# Prime num
# [2, 3, 5, 7,  11, 13, 17, 19]

# Non Prime num
# [1, 4, 6, 8, 9, 12, 14, 16, 18, 20]

import math


def is_prime_v1(num) -> bool:
    if num <= 1:
        return False

    for i in range(2, num):
        if num % i == 0:
            return False

    return True


def is_prime_v2(num: int) -> bool:
    """
    36 = 1* 36
    36 = 2* 18
    36 = 3* 12
    36 = 4* 9
    36 = 6* 6 <- √n
    """
    if num <= 1:
        return False

    for i in range(2, math.floor(math.sqrt(num) + 1)):
        if num % i == 0:
            return False

    return True


if __name__ == '__main__':
    import random
    import time

    numbers = [random.randint(0, 1000) for _ in range(100000)]
    start = time.time()

    for num in numbers:
        is_prime_v1(num)
    print('v1', time.time() - start)

    start = time.time()
    for num in numbers:
        is_prime_v2(num)
    print('v2', time.time() - start)
