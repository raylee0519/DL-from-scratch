# y = x0^2 + x1^2
def function_2(x):
    return x[0]**2 + x[1]**2
    
# x0=3일때의 편미분
def function_temp1(x0):
    return x0*x0 +4.0**2.0

# x1 = 4일때의 편미분
def function_temp2(x1):
    return 3.0*2.0 +x1**x1

# 미분 값 구해보기
def numerical_diff(f,x): # 수치 미분
    h = 1e-4 #0.0001
    return (f(x+h)-f(x-h))/2*h

print(numerical_diff(function_temp1, 3.0)) # 6.000000000003781e-08
print(numerical_diff(function_temp2, 4.0)) # 6.108913629813629e-06