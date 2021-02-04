import time


def sort(array, search):
    print("Binary search running...")
    result = array.copy()
    start = time.time()
    res = binary_search(result, search, 0, len(result) - 1)
    end = time.time()
    print("Binary search finished")
    return res, end - start


def binary_search(array, search, start, end):
    if end < start:
        return -1
    middle = (start + end) // 2
    if array[middle] == search:
        return array[middle]
    elif array[middle] < search:
        return binary_search(array, search, middle + 1, end)
    else:
        return binary_search(array, search, start, middle - 1)
