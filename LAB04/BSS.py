import random
from collections import Counter
import re

def is_primal(liczba):

    for i in range(2, int(liczba/2)):
        if liczba % i == 0:
            return False
    return True


def is_ok(liczba):
    return True if liczba % 4 == 3 else False


def find(liczba):

    base = liczba + 1

    while not ((is_primal(base) is True) and (is_ok(base) is True)):
        base = base + 1

    return base


def is_relatively_first(n, x):

    lower = min(n, x)

    for i in range(2, int(lower/2)):
        if n % i == 0:
            if x % i == 0:
                return False
    return True


def test1(series):
    cnt = Counter(series)

    if 9725 < cnt['1'] < 10275:
        return "PASSED"
    else:
        return "FAILED"


def test2(series):

    def passed(sign, string):
        keep_count = {}

        s = re.findall(f"{sign}+", string)

        for i in s:
            try:
                keep_count[len(i)] = keep_count[len(i)] + 1
            except KeyError:
                keep_count[len(i)] = 1

        suma_6_i_wiecej = 0

        for k in keep_count.keys():
            if k >= 6:
                suma_6_i_wiecej = suma_6_i_wiecej + keep_count[k]

        if ((2315 < keep_count[1] < 2685)
                and (1114 < keep_count[2] < 1386)
                and (527 < keep_count[3] < 723)
                and (240 < keep_count[4] < 384)
                and (103 < keep_count[5] < 209)
                and (103 < suma_6_i_wiecej < 209)):
            return True
        else:
            return False

    string = ""

    for i in series:
        string = string + i

    if passed("1", string) and passed("0", string):
        return "PASSED"
    else:
        return "FAILED"


def test3(series):

    def passed(sign, string):

        keep_count = {}

        s = re.findall(f"{sign}+", string)

        for i in s:
            try:
                keep_count[len(i)] = keep_count[len(i)] + 1
            except KeyError:
                keep_count[len(i)] = 1

        for k in keep_count.keys():
            if k >= 26:
                return False
        return True

    string = ""

    for i in series:
        string = string + i

    if passed("1", string) and passed("0", string):
        return "PASSED"
    else:
        return "FAILED"


def test4(series):

    firsty = series[::4]
    secondy = series[1::4]
    thirdy = series[2::4]
    fourthy = series[3::4]

    fours = []

    for a, b, c, d in zip(firsty, secondy, thirdy, fourthy):
        fours.append(a + b + c + d)

    cnt = Counter(fours)

    sums = 0

    for key, value in cnt.items():
        sums = sums + pow(value, 2)

    x = 16/5000 * sums - 5000

    if 2.16 < x < 46.17:
        return "PASSED"
    else:
        return "FAILED"


if __name__ == '__main__':

    random_series = []

    p = find(40000)
    q = find(p)
    print("P: ", p)
    print("Q: ", q)
    N = p*q
    x = random.randint(1, N - 1)
    while not is_relatively_first(N, x):
        x = random.randint(1, N - 1)
    x = 1560615539

    print("N: ", N)
    print("X: ", x)

    w_pierwotna = pow(x, 2) % N

    random_series.append(bin(w_pierwotna)[-1])

    # dlugosc = input("Ile bitów wylosować")
    dlugosc = 20000

    new_x = w_pierwotna

    for i in range(1, dlugosc):

        new_x = pow(new_x, 2) % N
        get_bit = bin(new_x)[-1]

        random_series.append(get_bit)

    print("TEST 1: ", test1(random_series))
    print("TEST 2: ", test2(random_series))
    print("TEST 3: ", test3(random_series))
    print("TEST 4: ", test4(random_series))
