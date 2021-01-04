import time


def sort(array):
    print("Merge sort running...")
    start = time.time()
    result = mergesort(array)
    end = time.time()
    print("Merge sort finished")
    return result, end - start


def mergesort(array):
    if len(array) <= 1:
        return array
    else:
        left_array = array[:len(array) // 2]
        right_array = array[len(array) // 2:]
        left_array = mergesort(left_array)
        right_array = mergesort(right_array)
        return merge(left_array, right_array)


def merge(left_array, right_array):
    array = []
    l_index = 0
    r_index = 0
    full_len = len(left_array) + len(right_array)
    for _ in range(0, full_len):
        if l_index < len(left_array) and r_index < len(right_array):
            if left_array[l_index] < right_array[r_index]:
                array.append(left_array[l_index])
                l_index += 1
            elif right_array[r_index] < left_array[l_index]:
                array.append(right_array[r_index])
                r_index += 1
            else:
                array.append(left_array[l_index])
                array.append(right_array[r_index])
                l_index += 1
                r_index += 1
        elif l_index < len(left_array) and r_index >= len(right_array):
            for i in range(l_index, len(left_array)):
                array.append(left_array[i])
            break
        elif l_index >= len(left_array) and r_index < len(right_array):
            for i in range(r_index, len(right_array)):
                array.append(right_array[i])
            break
    return array
