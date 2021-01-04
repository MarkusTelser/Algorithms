from sorting_algorithm import *
from random import *


# method to create test arrays
def random_data(length, start, end):
    data = []
    for i in range(0, length):
        data.append(int(random() * (end + 1) - start))
    return data


# method to run all sort algorithm
def run():
    array = random_data(10000, 0, 1000)

    names = ["Selection sort", "Insertion sort", "Merge sort", "Bubble sort", "Comb sort", "Counting sort",
             "Bucket sort", "Heap sort", "Shell sort"]
    times = [selection_sort.sort(array)[1], insertion_sort.sort(array)[1], merge_sort.sort(array)[1],
             bubble_sort.sort(array)[1], comb_sort.sort(array)[1], counting_sort.sort(array)[1],
             bucket_sort.sort(array)[1], heap_sort.sort(array)[1], shell_sort.sort(array)[1]]
    # sort and sync with names
    times, names = zip(*sorted(zip(times, names)))

    # print order of fastest sorting algorithms
    print("Sort algorithms:")
    for i in range(len(times)):
        print(str(i + 1) + ".", names[i], "-", times[i])
