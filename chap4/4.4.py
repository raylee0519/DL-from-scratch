# 기울기 구현
import numpy as np

def numerucal_gradient(f,x):
    h = 1e-4  #0.0001
    # x와 형상이 같은 배열에 모두0인 값
    grad = np.zeros_like(x)

    for idx in range(x.size):
        tmp_val = x[idx]
        # f(x+h) 계산
        x[idx] = tmp_val+h
        fxh1 = f(x)

        # f(x-h) 계산
        x[idx] = tmp_val-h
        fxh2 = f(x)    

        grad[idx] = (fxh1-fxh2)/(2*h)
        x[idx] = tmp_val
    return grad



def function_2(x):
    return np.sum(x**2)

print(numerucal_gradient(function_2, np.array([3.0,4.0]))) # [6. 8.]
print(numerucal_gradient(function_2, np.array([0.0,2.0]))) # [0. 4.]
print(numerucal_gradient(function_2, np.array([3.0,0.0]))) # [6. 0.]