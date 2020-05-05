def buble_sort(a_list):
    '''
    >>> buble_sort([6,5,4,3,2,1])
    [1, 2, 3, 4, 5, 6]
    >>> buble_sort([4,4,4,4])
    [4, 4, 4, 4]
    >>> buble_sort([])
    []
    >>> buble_sort([1])
    [1]
    >>> buble_sort([1,2])
    [1, 2]
    >>> buble_sort([2, 1])
    [1, 2]
    '''
    # My solution:
    # for k in range(len(a_list)):
    #     for i in range(len(a_list) - k - 1):
    #         if a_list[i] > a_list[i+1]:
    #             a_list[i], a_list[i+1] = a_list[i+1], a_list[i]
    # return a_list

    # From the book:
    unsorted_until_index = len(a_list) - 1
    issorted = False
    while not issorted:
        issorted = True
        for i in range(unsorted_until_index):
            if a_list[i] > a_list[i+1]:
                issorted = False
                a_list[i], a_list[i+1] = a_list[i+1], a_list[i]
        unsorted_until_index = unsorted_until_index - 1
    return a_list

def selection_sort(a_list):
    '''
    >>> selection_sort([6,5,4,3,2,1])
    [1, 2, 3, 4, 5, 6]
    >>> selection_sort([4,4,4,4])
    [4, 4, 4, 4]
    >>> selection_sort([])
    []
    >>> selection_sort([1])
    [1]
    >>> selection_sort([1,2])
    [1, 2]
    >>> selection_sort([2, 1])
    [1, 2]
    '''
    # My solution:
    # for i in range(len(a_list)):
    #     min, pos = None, None
    #     for k in range(i, len(a_list)):
    #         if min is None or a_list[k] < min:
    #             min, pos = a_list[k], k
    #     if pos != i:
    #         a_list[i], a_list[pos] = a_list[pos], a_list[i]
    # return a_list

    # From the book:
    for i in range(len(a_list)):
        lowestNumberIndex = i
        for k in range(i+1, len(a_list)):
            if a_list[k] < a_list[lowestNumberIndex]:
                lowestNumberIndex = k
        if lowestNumberIndex != i:
            a_list[i], a_list[lowestNumberIndex] = a_list[lowestNumberIndex], a_list[i]
    return a_list


def insertion_sort(a_list):
    '''
    >>> insertion_sort([6,5,4,3,2,1])
    [1, 2, 3, 4, 5, 6]
    >>> insertion_sort([4,4,4,4])
    [4, 4, 4, 4]
    >>> insertion_sort([])
    []
    >>> insertion_sort([1])
    [1]
    >>> insertion_sort([1,2])
    [1, 2]
    >>> insertion_sort([2, 1])
    [1, 2]
    >>> insertion_sort([4, 3, 7, 1, 7])
    [1, 3, 4, 7, 7]
    >>> insertion_sort([4,5,7,8,2,1,5,9,5,0,3,4,2,8,5,4])
    [0, 1, 2, 2, 3, 4, 4, 4, 5, 5, 5, 5, 7, 8, 8, 9]
    '''
    # My solution:
    # for i in range(1, len(a_list)):
    #     val = a_list[i]
    #     for k in range(i-1, -1, -1):
    #         if a_list[k] > val:
    #             a_list[k+1] = a_list[k]
    #             a_list[k] = val
    #         else:
    #             a_list[k+1] = val
    #             break
    # return a_list

    # From the book:
    for i in range(1, len(a_list)):
        pos, val = i, a_list[i]
        while pos > 0 and a_list[pos-1] > val:
            a_list[pos] = a_list[pos-1]
            pos -= 1
        a_list[pos] = val
    return a_list
