# 미분
import numpy as np

def numerical_diff_first(f,x): # 실제 미분 -> 너무 작은 값으로 만들면 오류 발생
    h = 10e-50 
    return (f(x+h)-f(x))/h

print(np.float32(1e-50))

def numerical_diff(f,x): # 수치 미분 -> 오차까지 줄이기
    h = 1e-4 #0.0001
    return (f(x+h)-f(x-h))/2*h