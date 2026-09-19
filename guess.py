import random as r
import math

def make_random(digits):
    rand = []
    for i in range(digits):
        rand.append(r.randint(0, 9))
    fnum = "".join(map(str, rand))
    return int(fnum)

def is_special(num):
    mult = 0
    special = False
    listed = list(str(num))
    conditions = []

    # same
    first = listed[0]
    check_same = True

    for i in range(1, len(listed)):
        if listed[i] != first:
            check_same = False
            break

    if check_same:
        mult += 1
        special = True
        conditions.append("Repeat")

    # palindromic
    if listed == listed[::-1] and len(listed) > 2:
        mult += 1
        special = True
        conditions.append("Palindromic")

    # prime
    is_prime = num >= 2

    if num % 2 == 0 and num != 2:
        is_prime = False
    else:
        mdiv = math.isqrt(num)

        for i in range(3, mdiv + 1, 2):
            if num % i == 0:
                is_prime = False
                break

    if is_prime:
        special = True
        mult += 1
        conditions.append("Prime")

    fconditions = " ".join(conditions)

    return special, mult, fconditions, num

a, b, c, d = is_special(make_random(2))
print(f"is it special? {a} multiplier: {b} conditions: {c} number: {d}")
