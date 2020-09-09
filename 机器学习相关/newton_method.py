# --------------------------------------
# Author: BlossomingL
# datetime 2020/9/9 11:19
# --------------------------------------

def f(x):
    return x ** 2 - 3


def f_grad(x):
    return 2 * x


def newton():
    x = 1
    eps = 1e-5
    error = 1
    while error > eps:
        tmp = x
        x = x - f(x) / f_grad(x)
        error = abs(x - tmp)
    print(x)


def main():
    newton()


if __name__ == '__main__':
    main()
