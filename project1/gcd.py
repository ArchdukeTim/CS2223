import functools
import math
import operator
import sys
import time


def euclid(m, n):
    while n:
        r = m % n
        m, n = n, r
    return m


def consecutive_integer(m, n):
    t = min(m, n)
    while True:
        if m % t == 0 and n % t == 0:
            return t
        t -= 1


def ms_procedure(m, n):
    m_primes = _get_primes(m)
    n_primes = _get_primes(n)

    primes = intersect(m_primes, n_primes)
    return functools.reduce(operator.mul, primes, 1)


def intersect(m, n):
    primes = m[:]
    for prime in m:
        if prime in n:
            n.remove(prime)
        else:
            primes.remove(prime)
    return primes


def _get_primes(x):
    primes = []
    while x % 2 == 0:
        primes.append(2)
        x //= 2
    for i in range(3, int(math.sqrt(x)) + 1, 2):
        while x % i == 0:
            primes.append(i)
            x //= i
    if x > 2:
        primes.append(x)
    return primes


def effGCD(m, n):
    now = time.perf_counter()
    val = euclid(m, n)
    print(val, time.perf_counter() - now)
    now = time.perf_counter()
    val = consecutive_integer(m, n)
    print(val, time.perf_counter() - now)
    now = time.perf_counter()
    val = ms_procedure(m, n)
    print(val, time.perf_counter() - now)

if __name__ == "__main__":
    if len(sys.argv) > 1:
        if sys.argv[1] == 'test':
            run_test()
            exit(0)
    while True:
        tries = 3
        while tries:
            try:
                m = int(input("Input first number: "))
            except ValueError:
                m = None
                print("Please input a non-zero number")
                tries -= 1
                continue

            if m == 0:
                m = None
                print("You cannot input 0")
                tries -= 1
            else:
                break

        while tries:
            try:
                n = int(input("Input second number: "))
            except ValueError:
                print("Please input a non-zero number")
                tries -= 1
                continue

            if n == 0:
                n = None
                print("You cannot input 0")
                tries -= 1
            else:
                break

        if not (m and n):
            print("Goodbye")
            exit(0)

        effGCD(m, n)
