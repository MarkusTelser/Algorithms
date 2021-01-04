from sorting_algorithm import insertion_sort
from sorting_algorithm import selection_sort
from sorting_algorithm import merge_sort
from sorting_algorithm import bubble_sort
from sorting_algorithm import comb_sort
from sorting_algorithm import counting_sort
from sorting_algorithm import bucket_sort
from sorting_algorithm import heap_sort
from random import *


# methode to create test arrays
def random_data(length, start, end):
    data = []
    for i in range(0, length):
        data.append(int(random() * (end + 1) - start))
    return data


array = random_data(10, 0, 10)
# testing sort algorithm
print("Selection sort:", selection_sort.sort(array)[1])
print("Insertion sort:", insertion_sort.sort(array)[1])
print("Merge sort:", merge_sort.sort(array)[1])
print("Bubble sort:", bubble_sort.sort(array)[1])
print("Comb sort:", comb_sort.sort(array)[1])
print("Counting sort:", counting_sort.sort(array)[1])
print("Bucket sort:", bucket_sort.sort(array)[1])
print("Bucket sort:", bucket_sort.sort(array)[1])

# search algo = A*
