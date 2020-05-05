def intersection(a_list, b_list):
    '''
    >>> intersection([1, 2, 3, 4],[4, 5, 6, 2, 3])
    [2, 3, 4]
    >>> intersection([1, 2, 3, 4],[5, 6, 7, 8])
    []
    >>> intersection([],[1])
    []
    >>> intersection([1, 1, 1, 1],[1, 0, 4])
    [1]
    '''
    first, second, result = None, None, list()
    if len(a_list) < len(b_list):
        first, second = set(a_list), set(b_list)
    else:
        first, second = set(b_list), set(a_list)

    for elem in first:
        if elem not in result and elem in second:
            result.append(elem)
    return result
