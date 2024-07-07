import numpy as np

# 항등 함수 구현
def identity_func(x):
    return x

# 소프트맥스 함수 구현
def softmax_before(a):
    exp_a = np.exp(a)
    sum_exp_a = np.sum(exp_a)
    y = exp_a/sum_exp_a
    return y

# 오버플로우를 막기위해 개선된 방법
def softmax_after(a):
    c= np.max(a)
    exp_a = np.exp(a-c)
    sum_exp_a = np.sum(exp_a)
    y = exp_a/sum_exp_a
    return y


a= np.array([0.3, 2.9,4.0])
y = softmax_after(a)

print(y)
print(np.sum(y)) # 1.0 - 소프트맥스 함수의 특징 : 총 합이 1