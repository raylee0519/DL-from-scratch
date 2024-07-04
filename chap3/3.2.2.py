# 계단 함수 표현
import numpy as np

def step_function(x) :
    y = x > 0
    return y.astype(np.int) # numpy 자료형을 변환할 때 사용 (int형으로 출력하기 위함)
