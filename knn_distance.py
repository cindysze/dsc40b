import random

def knn_distance(arr, q, k):
    for i in range(len(arr)):
        arr[i] = (abs(arr[i] - q), arr[i])

    def partition(left, right, pivot_index):
        pivot = arr[pivot_index]
        arr[pivot_index], arr[right] = arr[right], arr[pivot_index]

        store_index = left
        for i in range(left, right):
            if arr[i][0] < pivot[0]:
                arr[store_index], arr[i] = arr[i], arr[store_index]
                store_index += 1

        arr[right], arr[store_index] = arr[store_index], arr[right]
        return store_index

    def quickselect(left, right, k_smallest):
        if left == right:
            return arr[left]

        pivot_index = random.randint(left, right)
        pivot_index = partition(left, right, pivot_index)

        if k_smallest == pivot_index:
            return arr[k_smallest]
        elif k_smallest < pivot_index:
            return quickselect(left, pivot_index - 1, k_smallest)
        else:
            return quickselect(pivot_index + 1, right, k_smallest)

    result = quickselect(0, len(arr) - 1, k - 1)
    return result