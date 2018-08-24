import numpy as np
from re_svd import svdRec


Data1 = svdRec.load_exdata()
Data2 = svdRec.loadExData()
U, Sigma, VT = np.linalg.svd(Data1)

print('U:%s' % U)
print('Sigma:%s' % Sigma)
print('VT:%s' % VT)

# 将sigma向量变成对角矩阵
Sig3 = np.mat([[Sigma[0], 0, 0], [0, Sigma[1], 0], [0, 0, Sigma[2]]])
tmp = U[:, :3]*Sig3*VT[:3, :]
print(Data1)
print(tmp)


