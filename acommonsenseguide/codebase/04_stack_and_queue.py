def closing_parenthesis(str):
    '''
    >>> closing_parenthesis('(​ var​ x = [1, 2, 3)];')
    'Wrong closing brace ")" at 20 position'
    >>> closing_parenthesis("(​ var​ x = [1, 2, 3, {4}]);")
    'Correct'
    >>> closing_parenthesis("(​ var​ x = 1, 2, 3);")
    'Correct'
    >>> closing_parenthesis("[var​ x = 1, 2, 3]{];")
    'Wrong closing brace "]" at 19 position'
    >>> closing_parenthesis("[ var​ x = 1, 2, 3]")
    'Correct'
    >>> closing_parenthesis('(aweir')
    'No closing brace'
    >>> closing_parenthesis(')nj')
    'Wrong closing brace ")" at 0 position'
    >>> closing_parenthesis('qwierada')
    'Correct'
    >>> closing_parenthesis('')
    'Correct'
    '''
    # My solution:
    # stack = list()
    # braces = {')': '(', ']': '[', '}': '{'}
    # for ch in str:
    #     if ch in '([{':
    #         stack.append(ch)
    #     elif ch in ')]}':
    #         if stack and braces[ch] == stack[-1]:
    #             stack.pop()
    #         else:
    #             return 'Not correct'
    # if stack:
    #     return 'Not correct'
    # else:
    #     return 'Correct'

    # From the book:
    # stack = list()
    # braces = {')': '(', ']': '[', '}': '{'}
    # for i, ch in enumerate(str):
    #     if ch in '([{':
    #         stack.append(ch)
    #     elif ch in ')]}':
    #         if stack and braces[ch] == stack[-1]:
    #             stack.pop()
    #         else:
    #             return 'Wrong closing brace "{0}" at {1} position'.format(ch, i)
    # if stack:
    #     return 'No closing brace'
    # else:
    #     return 'Correct'

    # Pythonic way
    from queue import LifoQueue

    stack = LifoQueue(maxsize=0)
    #print(stack.qsize())
    braces = {')': '(', ']': '[', '}': '{'}
    for i, ch in enumerate(str):
        if ch in '([{':
            stack.put(ch)
        elif ch in ')]}':
            if not (not stack.empty() and braces[ch] == stack.get()):
                return 'Wrong closing brace "{0}" at {1} position'.format(ch, i)
    if not stack.empty():
        return 'No closing brace'
    else:
        return 'Correct'


def printer_queue(a_list):
    '''
    >>> printer_queue(['1', '2', '3'])
    1
    2
    3
    >>> printer_queue([])
    '''
    from queue import Queue
    que = Queue(maxsize=3)
    for task in a_list:
        que.put(task)

    while not que.empty():
        print(que.get())
