# 신경망에서의 기울기 구현
import sys, os
sys.path.append("../DL-from-scratch")  # 부모 디렉터리의 파일을 가져올 수 있도록 설정
import numpy as np
from common.functions import softmax, cross_entropy_error
from common.gradient import numerical_gradient

class simpleNet:
    def __init__(self):
        self.W = np.random.randn(2,3) # 정규분포로 초기화

    def predict(self, x):
        return np.dot(x, self.W)

    def loss(self, x, t):
        z = self.predict(x)
        y = softmax(z)
        loss = cross_entropy_error(y, t)
        return loss

x = np.array([0.6, 0.9])
t = np.array([0, 0, 1])

net = simpleNet()

f = lambda w: net.loss(x, t) # lambda : 단 하나의 코드를 작성하기 위한 함수 만들 때 사용 (이름도 부여 x)
dW = numerical_gradient(f, net.W) # 기울기 구하는 함수

print(dW)