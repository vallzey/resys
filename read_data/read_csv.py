import pandas as pd
from scipy import sparse
import numpy as np


def read_csv_as_sparse(filename, row_num, col_num, data_num):
    data_frame = pd.read_csv(filename)
    mat = data_frame.values.T
    row = mat[row_num].astype('int')
    col = mat[col_num].astype('int')
    data = mat[data_num]
    matrix = sparse.coo_matrix((data, (row, col)))
    return matrix.toarray()


# row = [1, 1, 2, 2, 3, 4, 4]
# # col = mat[col_num]
# col = [1, 3, 1, 2, 4, 2, 4]
# # data = mat[data_num]
# data = [2.5, 3, 3, 2, 4, 2, 2]
# matrix = sparse.coo_matrix((data, (row, col)))
# print(matrix)
#
# row = [2, 3, 3, 2]
# col = [3, 4, 2, 4]
# data = [1, 2, 3, 10]
# c = sparse.coo_matrix((data, (row, col)))
# # 如果去掉shape,矩阵默认row and col bigest
#
# print(c.col, c.row, c.data)
# print(c)
