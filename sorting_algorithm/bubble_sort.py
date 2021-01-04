import time


def sort(array):
    print("Bubble sort running...")
    start = time.time()
    result = array.copy()
    while True:
        sorted = False
        for i in range(1, len(result)):
            if result[i] < result[i - 1]:
                sorted = True
                x, y = result[i - 1], result[i]
                result[i], result[i - 1] = x, y
        if not sorted:
            break
    end = time.time()
    print("Bubble sort finished")
    return result, end - start
