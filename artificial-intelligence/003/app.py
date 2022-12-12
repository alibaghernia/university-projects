from copy import deepcopy


def isBakhshpazir(n):
    return n % 2 == 0 or n % 3 == 0


def isTavali(t):
    return isBakhshpazir(t) and isBakhshpazir(t-1) and isBakhshpazir(t-2)


def test(n, l=[]):
    list_ = deepcopy(l)

    if n <= 3:
        return list_

    if isTavali(n):
        list_.append([n, n-1, n-2])

    return test(n-1, list_)
