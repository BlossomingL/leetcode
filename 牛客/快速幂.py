def quick_pow_recursive(a, n):
    """
    递归求a^n
    :param a: 底数
    :param n: 幂
    :return:
    """
    if n == 0:
        return 1
    elif n & 1 == 1:
        return a * quick_pow_recursive(a, n - 1)
    else:
        tmp = quick_pow_recursive(a, n // 2)
        return tmp ** 2


def quick_pow_non_recursive(a, n):
    res = 1
    while n:
        if n & 1:
            res *= a
        a *= a
        n = n >> 1
    return res


if __name__ == '__main__':
    # res = quick_pow_recursive(3, 5)
    res = quick_pow_non_recursive(2, 10)
    print(res)