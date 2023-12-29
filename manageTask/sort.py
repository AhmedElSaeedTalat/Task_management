def swap(listn, idx1, idx2):
    """ swap two element in the list"""
    temp = listn[idx1]
    listn[idx1] = listn[idx2]
    listn[idx2] = temp

def partition(listn, l, h):
    """ main function for quicksort algorithm"""
    i = j = l
    pivot = h
    while i < pivot:
        if listn[i] <= listn[pivot]:
            swap(listn, i, j)
            j += 1
        i += 1
    swap(listn, j, pivot)
    return j

def sort_values(listn, l, h):
    """ recursion algorithm """
    if l > h:
        return None
    pivot_index = partition(listn, l, h)
    sort_values(listn, l, pivot_index - 1)
    sort_values(listn, pivot_index + 1, h)