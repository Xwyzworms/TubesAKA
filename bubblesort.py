arr = [0.22, 0.99, 0.88,0.21,0.11]
def bubblesort(arr):
    for i in range(0,len(arr)):
        for j in range(0,len(arr) - i- 1):
            arr[j] , arr[j+1] = arr[j+1] , arr[j]

    print(arr)
bubblesort(arr)
