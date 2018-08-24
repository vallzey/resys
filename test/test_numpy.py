import numpy as np
from re_svd import svdRec
from scipy import sparse


def test_nonzero():
    a = np.array([1, 2, 3, 0, 1, 0])

    # 用于返回数组中不为0的数字的下标
    m = np.nonzero(a)

    print(m)
    # 结果:(array([0, 1, 2, 4]),)


def test_a():
    data = np.mat(svdRec.load_exdata())
    print(data[:, (1, 3, 4)].A)
    print(data)


def test_a2():
    data = np.mat(svdRec.load_exdata())
    tmp = np.logical_and(data[:, 1].A > 0, data[:, 2].A > 0)
    overLap = np.nonzero(tmp)[0]
    print(overLap)


def test_logical_and():
    a = np.array([1, 1, 2, 0, 0, 0, 0])
    b = np.array([1, 0, 1, 0, 1, 0, 0])
    c = np.logical_and(a == 0, b == 0)
    print(c)
    # 结果:[False False False  True False  True  True]


def test_nonzero():
    b = np.array([1, 0, 1, 0, 1, 0, 0])
    c = np.nonzero(b == 0)
    print(c)
    # 结果:[False False False  True False  True  True]


def test_sparse():
    row = [2, 3, 3, 2]
    col = [3, 4, 2, 4]
    data = [1, 2, 3, 10]
    c = sparse.coo_matrix((data, (row, col)))
    # 如果去掉shape,矩阵默认row and col bigest

    print(c.col, c.row, c.data)
    print(c)


def test_sparse2():
    row = [2, 3, 3, 2]
    row = np.array(row)
    print(row.T)
    col = [3, 4, 2, 4]
    data = [1, 2, 3, 10]
    c = sparse.coo_matrix((data, (row, col)), shape=(5, 6))
    print(c.col, c.row, c.data)
    print(c.toarray())

test_sparse()
