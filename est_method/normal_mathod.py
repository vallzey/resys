import numpy as np


# 预测一个用户对一个物品的打分
def standEst(dataMat, user, simMeas, item):
    n = np.shape(dataMat)[1]  # 获取dataMat的列长度
    simTotal = 0.0
    ratSimTotal = 0.0
    for j in range(n):
        userRating = dataMat[user, j]
        if userRating == 0:
            continue
        overLap = np.nonzero(np.logical_and(dataMat[:, item].A > 0, dataMat[:, j].A > 0))[0]
        if len(overLap) == 0:
            similarity = 0
        else:
            similarity = simMeas(dataMat[overLap, item], dataMat[overLap, j])
        print('the %d and %d similarity is: %f' % (item, j, similarity))
        simTotal += similarity
        ratSimTotal += similarity * userRating
    if simTotal == 0:
        return 0
    else:
        return ratSimTotal / simTotal


# 使用svd,预测一个用户对一个物品的打分
def svdEst(dataMat, user, simMeas, item):
    n = np.shape(dataMat)[1]  # 获取dataMat的列长度
    simTotal = 0.0
    ratSimTotal = 0.0

    U, Sigma, VT = np.linalg.svd(dataMat)
    Sig4 = np.mat(np.eye(4) * Sigma[:4])
    xformedItems = dataMat.T * U[:, :4] * Sig4.I

    for j in range(n):
        userRating = dataMat[user, j]
        if userRating == 0 or j == item:
            continue

        similarity = simMeas(xformedItems[item, :].T, xformedItems[j, :].T)
        print('the %d and %d similarity is: %f' % (item, j, similarity))
        simTotal += similarity
        ratSimTotal += similarity * userRating
    if simTotal == 0:
        return 0
    else:
        return ratSimTotal / simTotal
