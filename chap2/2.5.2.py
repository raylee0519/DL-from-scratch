# 2.3.3 파일에서 게이트 import, 이때 2.3.3 파일을 model.py로 변경해야 import가능.
from model import NAND, OR, AND

def XOR(x1, x2):
    s1 = NAND(x1, x2)
    s2 = OR(x1, x2)
    y = AND(s1, s2)
    return y

print(XOR(0,0)) # 0
print(XOR(0,1)) # 1
print(XOR(1,0)) # 1
print(XOR(1,1)) # 0