import time

def bubble_sort(arr):
    """
        Keep swaping adjacent elements, until you don't need
        to swap anymore
    """
    sorted = False
    while sorted != True:
        for i in range(len(arr)-1):
            swap = False
            if arr[i+1] < arr[i]:
                arr[i+1], arr[i] = arr[i], arr[i+1]
                swap = True
        if swap == False:
            sorted = True
    return arr


def merge_sort(arr):
    """
        Divide the array into twos recursively, and sort the smallest pieces
    """
    def helper_merge_sort(arr, l, r):
        left = 0
        right = len(arr)-1
        m = len(arr)/2
        merge_sort(arr, )

    l = 0
    r = len(arr)-1
    m = (l+r)/2
    left = helper_merge_sort(arr, l, m)
    right = helper_merge_sort(arr, m+1, r)
    pass


def insertion_sort(arr):
    if len(arr) == 1:
        return arr
    for i in range(1, len(arr)):
        x = arr[i]
        j = i-1
        while j >= 0 and x < arr[j]:
            # keep moving elements up up from arr, until x > arr[j]
            arr[j+1] = arr[j]
            j -= 1
        arr[j+1] = x
    return arr


if __name__ in '__main__':
    A = [4,1,2, 454, 5,3, 20]
    print(insertion_sort(A))
    print(bubble_sort(A))