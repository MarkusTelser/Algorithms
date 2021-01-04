from sorting_algorithm import insertion_sort
import time


def sort(array):
    print("Bucket sort running...")
    start = time.time()
    result = []

    biggest_number = max(array)
    size = biggest_number / len(array)

    # Create n empty buckets where n is equal to the length of the input list
    buckets_list = []
    for x in range(len(array)):
        buckets_list.append([])

    # Put list elements into different buckets based on the size
    for i in range(len(array)):
        j = int(array[i] / size)
        if j != len(array):
            buckets_list[j].append(array[i])
        else:
            buckets_list[len(array) - 1].append(array[i])

    # Sort elements within the buckets using Insertion Sort
    for z in range(len(array)):
        buckets_list[z] = insertion_sort(buckets_list[z])

    # Concatenate buckets with sorted elements into a single list
    for x in range(len(array)):
        result = result + buckets_list[x]
    end = time.time()
    print("Bucket sort finished")
    return result, end - start


def insertion_sort(array):
    result = array.copy()
    for i in range(1, len(result)):
        paste = result[i]
        j = i
        while j > 0 and result[j - 1] > paste:
            result[j] = result[j - 1]
            j = j - 1
        result[j] = paste
    return result
