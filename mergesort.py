def merge(a, b):
    o = []
    while len(a) > 0 and len(b) > 0:
        if a[0] > b[0]:
            o.append(b.pop(0))
        else:
            o.append(a.pop(0))
    return o + a + b


def mergesort(a):
    if len(a) < 2:
        return a
    elif len(a) == 2:
        if a[0] > a[1]:
            return [a[1], a[0]]
        return a
    p = len(a) // 2
    return merge(mergesort(a[:p]), mergesort(a[p:]))


a_long = [int(i) for i in open("numbers.txt").read().splitlines()]
a = [5, 9, 1, 3, 4, 6, 6, 3, 2]
print(mergesort(a_long))
