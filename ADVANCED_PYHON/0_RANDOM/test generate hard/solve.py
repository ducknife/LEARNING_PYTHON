def solve(matrix):
    for i in range(len(matrix[0])):
        matrix[i].sort()
    return matrix