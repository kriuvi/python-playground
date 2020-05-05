def binary_search(ordered, elem):
    '''
    >>> binary_search([1,2,3,4,5,6,7,8,9], 7)
    6
    >>> binary_search([1,2,3,4,5,6,7,8,9], 2)
    1
    >>> binary_search([1,2,3,4,5,6,7,8,9], 0)
    >>> binary_search([], 1)
    '''
    lower_bound = 0
    upper_bound = len(ordered)-1
    while lower_bound <= upper_bound:
        mid = lower_bound + (upper_bound - lower_bound) // 2
        if ordered[mid] == elem:
            return mid
        if ordered[mid] < elem:
            lower_bound = mid + 1
        else:
            upper_bound = mid - 1
    return None
