def quicksort(arr, left=0, right=None):
    def partition(arr, left, right):
        pivot = left
        i = left + 1

        for j in range(i, right):
            if arr[j] < arr[pivot]:
                arr[i], arr[j] = arr[j], arr[i]
                i += 1

        arr[pivot], arr[i - 1] = arr[i - 1], arr[pivot]

        return i

    if len(arr) <= 1:
        return
    if right is None:
        right = len(arr)

    if left < right:
        pivot = partition(arr, left, right)
        quicksort(arr, left, pivot - 1)
        quicksort(arr, pivot + 1, right)



a = [10, 7, 3, 9, 1]
quicksort(a)
print(a)