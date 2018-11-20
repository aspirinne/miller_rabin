# Created by Rafael Galiev at 28.10.18

p = 2081  # simple number
q = 1301  # simple number

n = p*q


def nod(a, b):
    while a != 0 and b != 0:
        if a > b:
            a = a % b
        else:
            b = b % a

    return a + b


def odd(d):
    """Наибольший нечетный делитель"""
    if d % 2 == 0:
        d += 1

    for u in range(d-2, 1, -2):
        if d % u == 0:
            return float(u)


def grade(d):
    """наибольшая степень 2, на которую делится"""

    b = float(0)
    while d % 2 == 0:
        b += 1
        d /= 2

    return b


def witness_count(s, z):
    d = nod(z-1, s-1)
    u = odd(d)
    b = grade(d)

    count = float(u)**2 * ((4**float(b) - 1)/3 + 1)
    return count


# print(witness_count(p, q))
