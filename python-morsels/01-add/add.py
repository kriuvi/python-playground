def add_first(matrix1, matrix2):
    return [[r + p for r, p in zip(i, k)] for i, k in zip(matrix1, matrix2)]

def add_second(*args):
    collect = []
    leng = len(args[0])
    for i in range(leng):
        row = []
        for j in range(leng):
            total = 0
            for m in args:
                total += m[i][j]
            row.append(total)
        collect.append(row)
    print(collect)
    return collect

a = [[7, 8], [6, 5]]
b = [[-9, -9], [-7, -7]]
c = [[3, 3], [5, 5]]

def add(*matr):
    le = len(matr[0])
    for mat in matr:
        if len(mat) != le:
            raise ValueError('matrices size are not symmetric')
        for row in mat:
            if len(row) != le:
                raise ValueError('matrices size are not symmetric')
    return [[sum(val) for val in zip(*column)] for column in zip(*matr)]


print(add(a, b, c))

