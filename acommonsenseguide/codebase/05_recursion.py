def req_countdown(n):
    print(n)
    if n == 1:
        return 0
    else:
        return req_countdown(n-1)


def factorial(n):
    '''
    >>> factorial(5)
    120
    >>> factorial(3)
    6
    >>> factorial(0)
    'n cannot be <= 0'
    '''
    if n <= 0:
        return "n cannot be <= 0"
    if n == 1:
        return n
    else:
        return n * factorial(n-1)

def scan_dir(path = '/home/kriuvi/Downloads'):
    import os

    with os.scandir(path) as entries:
        for entry in entries:
            if entry.is_file():
                print(entry.name)
            if os.path.isdir(entry):
                print('->' + entry.name)
                scan_dir(entry)
