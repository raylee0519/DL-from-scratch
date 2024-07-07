# 3층 신경망 구현하기
# 입력(2개) ->1층(3개)->2층(2개)->출력층(2개)

import numpy as np
# A = [a1, a2,a3]
# X = [x1,x2]
# B = [b1,b2,b3]
# W = [w11 w21 w31], [w12 w22 w32]

X = np.array([1.0, 0.5])

W1 = np.array([[0.1,0.3,0.5],[0.2,0.4,0.6]])

B1 = np.array([0.1,0.2,0.3])

print(X.shape) # (2,)
print(W1.shape) # (2, 3)
print(B1.shape) # (3,)

A1 = np.dot(X,W1)+B1

print(A1) # [0.3 0.7 1.1]