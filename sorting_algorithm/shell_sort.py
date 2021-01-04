import time


def sort(array):
    print("Shell sort running...")
    start = time.time()
    result = array.copy()
    columns = [2147483647, 1131376761, 410151271, 157840433,
               58548857, 21521774, 8810089, 3501671, 1355339, 543749, 213331,
               84801, 27901, 11969, 4711, 1968, 815, 271, 111, 41, 13, 4, 1]
    for k in range(0, len(columns)):
        h = columns[k]
        # sort with insertion sort
        for i in range(h, len(result)):
            t = result[i]
            j = i
            while j >= h and result[j - h] > t:
                result[j] = result[j - h]
                j = j - h
            result[j] = t

    end = time.time()
    print("Shell sort finished")
    return result, end - start
