# 계단 함수의 그래프 표현
import numpy as np
import matplotlib.pylab as plt

def step_function(x) :
    return np.array(x > 0, dtype = np.int)

x = np.arange(-5.0, 5.0, 0.1) # -5 ~ 5까지 0.1 간격으로 생성
y = step_function(x)
plt.plot(x,y)
plt.ylim(-0.1, 1.1) # y축 범위 지정
plt.show()