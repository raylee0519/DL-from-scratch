# 경사 하강법

# init_x : 초기값
# lr  : learning rate 학습률
# step_num : 경사법에 따른 반복 횟수

import numpy as np

def gradient_descent(f, init_x, lr=0.01, step_num=100):
    x = init_x
    for i in range(step_num):
        grad = numerucal_gradient(f, x)
        x -= lr * grad
    return x

def numerucal_gradient(f, x):
    h = 1e-4  # 0.0001
    grad = np.zeros_like(x)

    for idx in range(x.size):
        tmp_val = x[idx]
        # f(x+h) 계산
        x[idx] = tmp_val + h
        fxh1 = f(x)

        # f(x-h) 계산
        x[idx] = tmp_val - h
        fxh2 = f(x)   
        grad[idx] = (fxh1 - fxh2) / (2 * h)
        x[idx] = tmp_val

    return grad

def function_2(x):
    return np.sum(x ** 2)

# 예제 : x0^2 + x1^2의 최소값
init_x = np.array([-3.0, 4.0])
res = gradient_descent(function_2, init_x=init_x, lr=0.1, step_num=100)

print(res) # [-6.11110793e-10  8.14814391e-10]