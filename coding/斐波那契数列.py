# 两方法建立斐波那契
# fibonacci
def fibonacci_1(n):
    if type(n) != int or n <= 0:
        return -1
    a, b = 1, 1
    # fib = [a]
    for x in range(n - 1):
        a, b = b, a + b
        # fib.append(a)
    return a


def fibonacci_2(n):
    if type(n) != int or n <= 0:
        return -1
    if n == 1 or n == 2:
        return 1
    return fibonacci_2(n - 1) + fibonacci_2(n - 2)


def print_fib(n):
    if type(n) != int or n <= 0:
        return False
    fib = []
    for x in range(1, n + 1):
        fib.append(fibonacci_2(x))
    return fib

if __name__ == '__main__':
    print(fibonacci_1(10))
    print(print_fib(10))