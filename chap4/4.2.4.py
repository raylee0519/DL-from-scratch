# 교차 엔트로피 오차 구현
# 1. 원-핫 인코딩 교차 엔트로피 오차 (One-hot)
# y는 신경망의 출력. t는 정답 레이블

import numpy as np

def cross_entropy_error(y,t):
    if y.ndim ==1:
        t = t.reshape(1,t.size)
        y = y.reshape(1,y.size)
    batch_size = y.shape[0]
    return -np.sum(t*np.log(y))/batch_size


# 2. 정답 레이블 교차 엔트로피 오차 (Not one-hot)
def cross_entropy_error2(y,t):
    if y.ndim ==1:
        t = t.reshape(1,t.size)
        y = y.reshape(1,y.size)
    batch_size = y.shape[0]
    return -np.sum(t*np.log(y[np.arange(batch_size),t]))/batch_size