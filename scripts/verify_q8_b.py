from sympy import symbols, expand, solve, simplify, Rational

# 定义符号变量
t = symbols('t')

# 计算均衡产量 (由于统一税率，国内外市场产量相同)
q = (12 - t)/3  # 每个企业在每个市场的产量
Q = 2*q  # 每个市场的总产量

# 计算均衡价格
P = 12 - Q  # 反需求函数

# 计算消费者剩余（只考虑国内市场）
CS = (Rational(1,2)) * Q * (12 - P)  # 需求曲线下方到均衡价格的面积
CS = expand(CS)

# 计算生产者剩余（考虑两个市场）
PS = 4 * (P - t) * q  # 4 = 2个企业 * 2个市场
PS = expand(PS)

# 计算税收收入（考虑两个市场）
TR = t * Q * 2  # 2表示两个市场
TR = expand(TR)

# 计算社会福利
W = expand(CS + PS + TR)

print("均衡产量Q:")
print(expand(Q))

print("\n均衡价格P:")
print(expand(P))

print("\n消费者剩余CS = (1/2)Q(12-P):")
print(f"= (1/2)({Q})({12-P})")
print(f"= {CS}")


print("\n生产者剩余PS = 4(P-t)q:")
print(f"= 4({P}-t)({q})")
print(f"= {PS}")

print("\n税收收入TR = 2tQ:")
print(f"= 2t({Q})")
print(f"= {TR}")

print("\n社会福利函数W = CS + PS + TR:")
print(W)

# 计算关于t的导数
dW_dt = W.diff(t)

print("\n关于t的导数:")
print(expand(dW_dt))

# 求解最优税率
solution = solve(dW_dt, t)
print("\n最优税率:")
print(f"t* = {expand(solution[0])}")

# 验证二阶条件
d2W_dt = dW_dt.diff(t)

print("\n二阶导数:")
print(f"d2W/dt^2 = {expand(d2W_dt)}") 