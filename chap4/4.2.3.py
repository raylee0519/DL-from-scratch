# 미니 배치
import sys
sys.path.append("../DL-from-scratch")
import numpy as np
from dataset.mnist import load_mnist

(x_train, t_train), (x_test, t_test) = load_mnist(normalize=True, one_hot_label=True)

print(x_train.shape) # (60000, 784)

print(t_train.shape) # (60000,10)

# 훈련 데이터는 60000개이고 입력데이터는 784열인 이미지 데이터

# 정답 레이블은 10줄짜리 데이터



# 무작위로 10장만 선택하기
# np.random.choice 는 지정한 범위의 수 중에서 무작위로 원하는 개수만 꺼낼 수 있다.
train_size = x_train.shape[0]
batch_size = 10
batch_mask = np.random.choice(train_size, batch_size)
x_batch = x_train[batch_mask]
t_batch = t_train[batch_mask]