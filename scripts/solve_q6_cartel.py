import sympy as sp
from sympy import diff, solve, symbols

# 定义符号变量
p1, p2 = symbols("p1 p2")

# 需求函数
q1 = 30 - 2*p1 - p2
q2 = 30 - 2*p2 - p1

# 价格协议下的总利润
profit = p1*q1 + p2*q2
profit = profit.expand()

# 对p1和p2求导
dp1 = diff(profit, p1)
dp2 = diff(profit, p2)

# 由对称性，p1 = p2 = p
p = symbols("p")
eq = dp1.subs([(p1,p), (p2,p)])

# 解一阶条件
p_cartel = solve(eq, p)[0]

# 计算均衡需求量和利润
q_cartel = 30 - 2*p_cartel - p_cartel
profit_cartel = 2*p_cartel*q_cartel

print(f"价格协议下的均衡：")
print(f"p = {p_cartel}")
print(f"q = {q_cartel}")
print(f"总利润 = {profit_cartel}") 