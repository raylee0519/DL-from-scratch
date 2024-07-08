# 교차 엔트로피 오차
import numpy as np

def cross_entropy_error(y,t):
    delta = 1e-7 # 아주 작은 값을 더해서 절대 0이 되지 않도록 설계
    return -np.sum(t*np.log(y+delta))

# 정답 레이블
t = [0,0,1,0,0,0,0,0,0,0] # 정답은 2

# 추론하여 나온 결과값이 2일 확률이 제일 높다고 나온경우 
y1 = [0.1,0.05,0.6,0.0,0.05,0.1,0.0,0.1,0.0,0.0]
print(cross_entropy_error(np.array(y1), np.array(t))) # 0.510825457099

# [틀린추론]추론하여 나온 결과값이 7일 확률이 제일 높다고 나온경우 
y2 = [0.1,0.05,0.1,0.0,0.05,0.1,0.0,0.6,0.0,0.0]
print(cross_entropy_error(np.array(y2), np.array(t))) # 2.30258409299