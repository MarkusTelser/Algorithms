import time


def sort(array, search):
    print("Linear search running...")
    result = array.copy()
    start = time.time()
    res = -1
    for i in range(len(array)):
        if array[i] == search:
            res = array[i]
            break
    end = time.time()
    print("Linear search finished")
    return res, end - start
