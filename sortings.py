def bubblesort(a):
    s = len(a)
    swapped = True
    i = 0
    while i < s - 1 and swapped is True:
        swapped = False
        for j in range(s - i - 1):
            if a[j] > a[j + 1]:
                a[j], a[j + 1] = a[j + 1], a[j]
                swapped = True
        i += 1


def selectionsort(a):
    n = len(a)

    for i in range(n):
        mx = 0
        for j in range(n - i):
            if a[j] > a[mx]:
                mx = j
        a[n - i - 1], a[mx] = a[mx], a[n - i - 1]


def insertionsort(a):
    for i in range(1, len(a)):
        key = a[i]
        j = i - 1

        while j >= 0 and key < a[j]:
            a[j + 1] = a[j]
            j -= 1
        a[j + 1] = key


def mergesort(a):
    if len(a) > 1:
        middle = len(a) // 2
        L = a[:middle]
        R = a[middle:]

        mergesort(L)
        mergesort(R)

        i = j = k = 0

        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                a[k] = L[i]
                i += 1
            else:
                a[k] = R[j]
                j += 1
            k += 1

        while i < len(L):
            a[k] = L[i]
            i += 1
            k += 1

        while j < len(R):
            a[k] = R[j]
            j += 1
            k += 1


def quicksort(a, left=0, right=None):
    def partition(a, left, right):
        pivot = left
        i = left + 1

        for j in range(i, right):
            if a[j] < a[pivot]:
                a[j], a[i] = a[i], a[j]
                i += 1
        a[pivot], a[i - 1] = a[i - 1], a[pivot]
        
        return i
    
    if len(a) <= 1:
        return
    if right is None:
        right = len(a)

    if left < right:
        p = partition(a, left, right)
        quicksort(a, left, p - 1)
        quicksort(a, p + 1, right)
    

a = [10, 5, 2, 6, 5, 0, 3, 10]
print(a)
# bubblesort(a)
# selectionsort(a)
# insertionsort(a)
# mergesort(a)
# quicksort(a)
print(a)
