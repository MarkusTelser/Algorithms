from sorting_algorithm import counting_sort
from search_algorithm import *
from random import *


# method to create test arrays
def random_data(length, start, end):
    data = []
    for i in range(0, length):
        data.append(int(random() * (end + 1) - start))
    data.sort()
    return data


# method to run all sort algorithm
def run():
    size = 1000000
    array = random_data(size, 0, 1000)
    search = array[int(random() * size)]
    names = ["Binary sort"]
    times = [binary_search.sort(array, search)[1]]
    # sort and sync with names
    times, names = zip(*sorted(zip(times, names)))
    # print order of fastest sorting algorithms
    print("\nSort algorithms:")
    for i in range(len(times)):
        print(str(i + 1) + ".", names[i], "-", times[i])

    # suggestion for algo to code
    # A* search algorithm
    # BM 25F
    # depth first search
    # breadth first search
    # brepth first search
    # deadth first search
