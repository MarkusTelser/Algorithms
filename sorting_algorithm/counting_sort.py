import time


def sort(array):
    print("Counting sort running...")
    start = time.time()
    result = [0] * len(array)
    smallest_number = array[0]
    biggest_number = array[0]
    # find smallest and biggest number
    for i in range(1, len(array)):
        if array[i] > biggest_number:
            biggest_number = array[i]
        if array[i] < smallest_number:
            smallest_number = array[i]
    # count every element and increment in count_array
    count_array = [0] * (biggest_number - smallest_number + 1)
    for i in range(0, len(array)):
        count_array[array[i] - smallest_number] += 1
    # modify array by adding previous count
    for i in range(1, len(count_array)):
        count_array[i] += count_array[i - 1]
    # place numbers in final array
    for i in range(len(array) - 1, -1, -1):
        result[count_array[array[i] - smallest_number] - 1] = array[i]
        count_array[array[i] - smallest_number] -= 1
    end = time.time()
    print("Counting sort finished")
    return result, end - start
