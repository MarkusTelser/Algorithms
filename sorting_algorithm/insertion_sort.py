import time


def sort(array):
    start = time.time()
    result = array.copy()
    for i in range(1, len(result)):
        paste = result[i]
        j = i
        while j > 0 and result[j - 1] > paste:
            result[j] = result[j - 1]
            j = j - 1
        result[j] = paste
    end = time.time()
    return result, end - start
