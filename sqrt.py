


def sqrt(a, q):
    if a < 0:
        return 'wrong!'
    if a <= 1:
        l = 0
        r = a + 0.25
    elif a > 2:
        l = 1
        r = a/2
    else:
        l = 1
        r = 2

    while l < r:
        min = (l+r)/2
        current = min ** 2
        res = a-current
        if res < 0:
            res = -res
        if res < q:
            return min
        if current > a:
            r = min
        else:
            l = min


if __name__ == '__main__':
    r = sqrt(1.21, 1e-3)
    print(r)

