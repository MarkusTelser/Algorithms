import time


def sort(array):
    print("Heap sort running...")
    start = time.time()
    result = array.copy()
    for i in range(len(result) // 2 - 1, -1, -1):
        heapify(result, len(result), i)

    # One by one extract elements
    for i in range(len(result) - 1, 0, -1):
        result[i], result[0] = result[0], result[i]  # swap
        heapify(result, i, 0)
    end = time.time()
    print("Heap sort finished")
    return result, end - start


def heapify(arr, n, i):
    largest = i
    left = 2 * i + 1
    right = 2 * i + 2

    # See if left child of root exists and is greater than root
    if left < n and arr[largest] < arr[left]:
        largest = left

    # See if right child of root exists and is greater than root
    if right < n and arr[largest] < arr[right]:
        largest = right

    # Change root, if needed
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        # Heapify the root.
        heapify(arr, n, largest)
