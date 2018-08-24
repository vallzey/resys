from re_sys import re_normal
from re_svd import svdRec
from re_sim import sim
import numpy as np


def test_standEst():
    data = svdRec.load_coo_matrix()
    # data = np.mat(data)
    rate = re_normal.standEst(data, 2, sim.cosSim, 3)
    print(rate)


def test_recommend():
    data = svdRec.load_exdata()
    data = np.mat(data)
    topN = re_normal.recommend(dataMat=data, user=2, estMethod=re_normal.standEst)
    print(topN)


test_standEst()
