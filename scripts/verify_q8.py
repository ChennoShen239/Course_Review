from sympy import symbols, solve, expand, simplify

# 定义符号变量
t1, t2, t = symbols('t1 t2 t')
q1d, q2d, q1f, q2f = symbols('q1d q2d q1f q2f')

# a) 分别征税的情况
print("验证a)部分:")

# 验证均衡产量
eq1 = 12 - 2*q1d - q2d - t1
eq2 = 12 - q1d - 2*q2d - t1
eq3 = 12 - 2*q1f - q2f - t2
eq4 = 12 - q1f - 2*q2f - t2

# 解一阶条件
sol = solve((eq1, eq2), (q1d, q2d))
print(f"均衡产量 q1d = q2d = {simplify(sol[q1d])}")

sol = solve((eq3, eq4), (q1f, q2f))
print(f"均衡产量 q1f = q2f = {simplify(sol[q1f])}")

# 验证社会福利函数
qd = (12-t1)/3
qf = (12-t2)/3
Qd = 2*qd
Qf = 2*qf

# 消费者剩余
CS = (1/2)*(12-Qd)*Qd
print(f"消费者剩余 CS = {expand(CS)}")

# 生产者剩余
PS = 2*((12-2*qd-t1)*qd + (12-2*qf-t2)*qf)
print(f"生产者剩余 PS = {expand(PS)}")

# 税收收入
TR = t1*Qd + t2*Qf
print(f"税收收入 TR = {expand(TR)}")

# 社会福利
W = CS + PS + TR
print(f"社会福利 W = {expand(W)}")

# 验证最优税率
dW_dt1 = W.diff(t1)
dW_dt2 = W.diff(t2)
print(f"dW/dt1 = {expand(dW_dt1)}")
print(f"dW/dt2 = {expand(dW_dt2)}")

opt_tax = solve((dW_dt1, dW_dt2), (t1, t2))
print(f"最优税率: t1* = {opt_tax[t1]}, t2* = {opt_tax[t2]}")

# b) 单一税率的情况
print("\n验证b)部分:")

# 验证均衡产量
eq1 = 12 - 2*q1d - q2d - t
eq2 = 12 - q1d - 2*q2d - t
eq3 = 12 - 2*q1f - q2f - t
eq4 = 12 - q1f - 2*q2f - t

sol = solve((eq1, eq2), (q1d, q2d))
print(f"均衡产量 q1d = q2d = {simplify(sol[q1d])}")

sol = solve((eq3, eq4), (q1f, q2f))
print(f"均衡产量 q1f = q2f = {simplify(sol[q1f])}")

# 验证社会福利函数
q = (12-t)/3
Q = 2*q

# 消费者剩余
CS = (1/2)*(12-Q)*Q
print(f"消费者剩余 CS = {expand(CS)}")

# 生产者剩余
PS = 4*(12-2*q-t)*q
print(f"生产者剩余 PS = {expand(PS)}")

# 税收收入
TR = 4*t*q
print(f"税收收入 TR = {expand(TR)}")

# 社会福利
W = CS + PS + TR
print(f"社会福利 W = {expand(W)}")

# 验证最优税率
dW_dt = W.diff(t)
print(f"dW/dt = {expand(dW_dt)}")

opt_tax = solve(dW_dt, t)
print(f"最优税率: t* = {opt_tax[0]}") 