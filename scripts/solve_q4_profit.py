import sympy as sp
from sympy import diff, solve, symbols, integrate

# 定义符号变量
p1, p2, v1, v2, t, L, x = symbols("p1 p2 v1 v2 t L x")
alpha1, alpha2, beta1, beta2 = symbols("alpha1 alpha2 beta1 beta2")

# 给定的均衡价格和市场分界点表达式
p1_eq = (v1 - v2)/3 + t*L
p2_eq = (v2 - v1)/3 + t*L
x_eq = (v1 - v2)/(6*t) + L/2

# 计算企业1的需求量(从0到x_eq的积分)
D1 = x_eq
# 计算企业2的需求量(从x_eq到L的积分)
D2 = L - x_eq

# 计算企业的利润
profit1 = p1_eq * D1
profit2 = p2_eq * D2

# 分析α型广告(差异化广告)的效果
# 当t增加时对利润的影响
dprofit1_dt = diff(profit1, t)
dprofit2_dt = diff(profit2, t)

print("α型广告(差异化广告)的效果:")
print(f"dπ1/dt = {dprofit1_dt}")
print(f"dπ2/dt = {dprofit2_dt}")
print("这表明当t增加时,两个企业的利润都会上升,因此α型广告具有正外部性\n")

# 分析β型广告(价值广告)的效果
# 当v1增加时对利润的影响
dprofit1_dv1 = diff(profit1, v1)
dprofit2_dv1 = diff(profit2, v1)

print("β型广告(价值广告)的效果:")
print(f"dπ1/dv1 = {dprofit1_dv1}")
print(f"dπ2/dv1 = {dprofit2_dv1}")
print("这表明当v1增加时,企业1的利润上升而企业2的利润下降,因此β型广告具有负外部性") 