#


def rec(a, b):
    if a == 0 or b == 0:
        return [a, b]
    elif a >= 2* b:
        return rec(a -2 * b, b)
    elif b >= 2 * a:
        return rec(a, b - 2 * a)
    else:
        return [a, b]

# print(rec(a=, b=))