# 평균 제곱 오차 (MSE)
import numpy as np
def mean_squared_error(y,t):
    return 0.5 * np.sum((y-t)**2)

# 정답 레이블 - 2인 이미지
t = [0,0,1,0,0,0,0,0,0,0]

# 추론하여 나온 결과값이 2일 확률이 제일 높다고 나온경우 (정답:2)
y1 = [0.1,0.05,0.6,0.0,0.05,0.1,0.0,0.1,0.0,0.0]
print(mean_squared_error(np.array(y1), np.array(t))) # 0.0975

# [틀린 추론] 추론하여 나온 결과값이 7일 확률이 제일 높다고 나온경우 (정답:2)
y2 = [0.1,0.05,0.1,0.0,0.05,0.1,0.0,0.6,0.0,0.0]
print(mean_squared_error(np.array(y2), np.array(t))) # 0.5975