import time


def sort(array):
    start = time.time()
    shrink = 1.3
    _gap = len(array)
    result = list(array)
    sorted = False
    while not sorted:
        _gap /= shrink
        gap = int(_gap)
        if gap <= 1:
            sorted = True
            gap = 1
        for i in range(len(array) - gap):
            sm = gap + i
            if result[i] > result[sm]:
                result[i], result[sm] = result[sm], result[i]
                sorted = False
    end = time.time()
    return result, end - start
