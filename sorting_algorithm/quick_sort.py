import time
import math


# not working

def sort(array):
    start = time.time()
    result = quicksort(array, 0, len(array) - 1)
    end = time.time()
    return result, end - start


def quicksort(array, low, high):
    if low < high:
        p = partition(array, low, high)
        quicksort(array, low, p)
        quicksort(array, p + 1, high)
    else:
        return array


def partition(array, low, high):
    pivot = array[high]
    i, j = low - 1, high
    while i <= j:
        if i < j and array[i] < pivot:
            i += 1
        if i <= j and array[j] >= pivot:
            j -= 1
        if i < j:
            x, y = array[i], array[j]
            array[i], array[j] = y, x

    x, y = array[low], array[j]
    array[low], array[j] = y, x
    return j
