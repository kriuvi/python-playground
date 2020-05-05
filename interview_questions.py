from collections import defaultdict


def firstDuplicate(a_str):
    '''
    Describe and code an algorithm that returns the first duplicate character in a string?
    >>> firstDuplicate('abbccd')
    'b'
    >>> firstDuplicate('')
    >>> firstDuplicate('bb')
    'b'
    >>> firstDuplicate('asd')
    >>> firstDuplicate('basdfb')
    'b'
    '''
    seen = list()
    for ch in a_str:
        if ch in seen:
            return ch
        else:
            seen.append(ch)
    return None

def removeDuplicates(a_list):
    '''
    In a given sorted array of integers remove all the duplicates.
    >>> removeDuplicates([1,2,3,3,4,4])
    [1, 2, 3, 4]
    >>> removeDuplicates([])
    []
    >>> removeDuplicates([1])
    [1]
    '''
    final_list = list()
    for el in a_list:
        if el not in final_list:
            final_list.append(el)
    return final_list

def uniqueNumbers(a_list):
    '''
    Find the unique numbers in an integer array?
    >>> uniqueNumbers([1,1,2,2,3,3,1])
    [1, 2, 3]
    >>> uniqueNumbers([1,1,1,1,1,3,4,5])
    [1, 3, 4, 5]
    >>> uniqueNumbers([1,1,1,1,1])
    [1]
    >>> uniqueNumbers([])
    []
    >>> uniqueNumbers([1])
    [1]
    '''
    #return list(set(a_list))
    seen = list()
    [seen.append(num) for num in a_list if num not in seen]
    return seen

def animal(num):
    '''
    >>> animal(24)
    'AN'
    >>> animal(5)
    5
    >>> animal(48)
    'ANIM'
    >>> animal(64)
    'ANIMAL'
    '''
    output = num
    if not num % 8:
        output = 'AN'
        num = num / 8
        if not num % 2:
            output += 'IM'
            num = num / 2
            if not num % 2:
                output += 'AL'
    return output

def secondLargest(a_list):
    '''
    From a given list of array (Not sorted) find the second largest value
    >>> secondLargest([5,6,9,1,3])
    6
    >>> secondLargest([])
    >>> secondLargest([1])
    >>> secondLargest([2,1])
    1
    >>> secondLargest([5,5,5])
    5
    >>> secondLargest([5,6,6,7,7])
    7
    '''
    first, second = None, None
    for num in a_list:
        if first is None or first < num:
            first, second = num, first
        elif second is None or second < num:
            second = num
    return second

def anagram(str1, str2):
    '''
    You have a two words which are an anagram of one another, write a program which can validate this
    >>> anagram('asd', 'dsa')
    True
    >>> anagram('asd', 'das')
    True
    >>> anagram('aaaas', 'aaas')
    False
    >>> anagram('', '')
    False
    >>> anagram('a', 'a')
    True
    >>> anagram('aa', 'aa')
    True
    >>> anagram('asD', 'dsa')
    False
    >>> anagram('asdd', 'adss')
    False
    '''
    if len(str1) != len(str2) or len(str1) == 0:
        return False
    dict1, dict2 = defaultdict(int), defaultdict(int)
    for ch1, ch2 in zip(str1, str2):
        dict1[ch1] += 1
        dict2[ch2] += 1
    return True if dict1 == dict2 else False

def palindrome(str1, str2):
    '''
    You have a two words which are a palindrome of one another, write a program which can validate this
    >>> palindrome('asd', 'dsa')
    True
    >>> palindrome('asd', 'das')
    False
    >>> palindrome('aaaas', 'aaas')
    False
    >>> palindrome('', '')
    False
    >>> palindrome('a', 'a')
    True
    >>> palindrome('aa', 'aa')
    True
    >>> palindrome('asD', 'dsa')
    False
    '''
    if len(str1) != len(str2) or len(str1) == 0:
        return False
    i, k = 0, len(str1)-1
    while i < len(str1):
        if str1[i] != str2[k]:
            return False
        i += 1
        k -= 1
    return True

def removeSubstrings(a_str, sub_str):
    '''
    Write a function that removes substrings.
    >>> removeSubstrings('', '')
    ''
    >>> removeSubstrings('', 'a')
    ''
    >>> removeSubstrings('asd', '')
    'asd'
    >>> removeSubstrings('absd', 'a')
    'bsd'
    >>> removeSubstrings('avsd', 's')
    'avd'
    >>> removeSubstrings('asfd', 'd')
    'asf'
    >>> removeSubstrings('asdd', 'd')
    'as'
    >>> removeSubstrings('asadadf', 'ad')
    'asf'
    >>> removeSubstrings('asadad', 'da')
    'asad'
    >>> removeSubstrings('asaDad', 'ad')
    'asaD'
    '''
    flag = False
    output = ''
    i, cur = 0, 0
    if len(a_str) == 0 or len(sub_str) == 0:
        return a_str
    str_len, sub_len = len(a_str), len(sub_str)
    while i < str_len:
        if (i + sub_len) <= str_len:
            cur = i
            for sub in sub_str:
                if a_str[cur] != sub:
                    flag = False
                    break
                else:
                    # print(cur)
                    cur += 1
                flag = True
        if flag:
            flag = False
            i += sub_len
            # print('a', i, cur, flag)
        else:
            output += a_str[i]
            i += 1
            # print('b', i, cur, flag)
    return output

def unique(a_list):
    '''
    Find the first unique integer in a list

    >>> unique([])
    >>> unique([1])
    1
    >>> unique([1,2])
    1
    >>> unique([1,2,3,4,5,6])
    1
    >>> unique([1, 2, 1])
    2
    >>> unique([2,3,4,2,4,3,5])
    5
    >>> unique([5,5,5])
    '''
    seen = list()
    duplicates = list()
    for num in a_list:
        if num not in seen and num not in duplicates:
            seen.append(num)
        elif num not in duplicates:
            seen.remove(num)
            duplicates.append(num)
    return seen[0] if len(seen) else None
