from scipy import sparse


def loadExData():
    return [[1, 1, 0, 2, 2],
            [0, 0, 0, 3, 3],
            [0, 0, 0, 1, 1],
            [1, 1, 1, 0, 0],
            [2, 2, 2, 0, 0],
            [5, 5, 5, 0, 0],
            [1, 1, 1, 0, 0]]


def load_exdata():
    return [[1, 1, 1, 0, 0],
            [2, 2, 2, 0, 0],
            [1, 1, 1, 0, 0],
            [5, 5, 5, 0, 0],
            [1, 1, 0, 2, 2],
            [0, 0, 0, 3, 3],
            [0, 0, 0, 1, 1]]


def load_coo_matrix():
    row = [2, 3, 3, 2]
    col = [3, 4, 2, 4]
    data = [1, 2, 3, 10]
    mat = sparse.coo_matrix(data, (row, col))
    return mat.toarray()
