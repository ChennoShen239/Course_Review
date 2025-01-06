import sympy as sp

# 定义变量
A, c, t, P = sp.symbols('A c t P')
Q = A - P

# 外国垄断企业的利润函数
profit = (P - c - t) * (A - P)

# 对P求导并令其等于0
dprofit_dP = sp.diff(profit, P)
P_star = sp.solve(dprofit_dP, P)[0]

# 计算均衡产量
Q_star = A - P_star

# 计算消费者剩余
CS = Q_star**2 / 2

# 计算关税收入
T = t * Q_star

# 计算本国福利
W = CS + T

# 对t求导并令其等于0
dW_dt = sp.diff(W, t)
t_star = sp.solve(dW_dt, t)[0]

print("最优价格:")
print(P_star)
print("\n最优产量:")
print(Q_star)
print("\n消费者剩余:")
print(CS)
print("\n关税收入:")
print(T)
print("\n本国福利:")
print(W)
print("\n最优关税:")
print(t_star) 