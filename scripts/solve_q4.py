import sympy as sp
from sympy import diff, solve, symbols

# 定义符号变量
p1, p2, v1, v2, t, L, x = symbols("p1 p2 v1 v2 t L x")
alpha1, alpha2, beta1, beta2 = symbols("alpha1 alpha2 beta1 beta2")

# 给定的均衡价格和市场分界点表达式
p1_eq = (v1 - v2)/3 + t*L
p2_eq = (v2 - v1)/3 + t*L
x_eq = (v1 - v2)/(6*t) + L/2

# 分析α型广告(差异化广告)的效果
# 假设t是α1和α2的函数: t = t(α1,α2)
# 当α1增加时,t增加,从而影响价格
dp1_dt = diff(p1_eq, t)  # p1对t的导数
dp2_dt = diff(p2_eq, t)  # p2对t的导数

print("α型广告(差异化广告)的效果:")
print(f"dp1/dt = {dp1_dt}")  # 应该为正
print(f"dp2/dt = {dp2_dt}")  # 应该为正
print("这表明当t增加时,两个企业的价格都会上升,因此α型广告具有正外部性\n")

# 分析β型广告(价值广告)的效果
# v1是β1的函数,v2是β2的函数
dp1_dv1 = diff(p1_eq, v1)  # p1对v1的导数
dp2_dv1 = diff(p2_eq, v1)  # p2对v1的导数

print("β型广告(价值广告)的效果:")
print(f"dp1/dv1 = {dp1_dv1}")  # 应该为正
print(f"dp2/dv1 = {dp2_dv1}")  # 应该为负
print("这表明当v1增加时,p1上升而p2下降,因此β型广告具有负外部性")
