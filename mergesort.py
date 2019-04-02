def mergesort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        L = arr[mid:]
        R = arr[:mid]

        i = j = k = 0

        mergesort(L)
        mergesort(R)

        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1
        
        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1

        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1

a = [10, 5, 3, 2, 5, 63, 2, 7]
b = "afjslaldkajkvnkswltk"
c = list(b)
mergesort(c)
c = ''.join(c)
print(c)