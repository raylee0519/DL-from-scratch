# 수치 미분 예시
import numpy as np
import matplotlib.pyplot as plt

def numerical_diff(f,x):
    h = 1e-4 #0.0001
    return (f(x+h)-f(x-h))/2*h 

def function_1(x):
    return 0.01*x**2 + 0.1*x # y=0.01x^2+0.1x

x = np.arange(0.0,20.0,0.1)
y = function_1(x)
plt.xlabel("x")
plt.ylabel("f(x)")
plt.plot(x,y)
plt.show()

# 미분 값 구해보기
def numerical_diff(f,x): # 수치 미분
    h = 1e-4 #0.0001
    return (f(x+h)-f(x-h))/2*h

print(numerical_diff(function_1,5)) # 1.9999999999908982e-09
print(numerical_diff(function_1,10)) # 2.999999999986347e-09