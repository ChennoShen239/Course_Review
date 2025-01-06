import sympy as sp
from sympy import diff, solve, symbols

# 定义符号变量
q1d, q2d, q1f, q2f = symbols("q1d q2d q1f q2f")  # d代表国内市场，f代表国际市场
t1, t2 = symbols("t1 t2")  # t1是内销税率，t2是出口税率

# a) 分别征税的情况
# 企业1的利润函数
profit1 = (12-(q1d+q2d)-t1)*q1d + (12-(q1f+q2f)-t2)*q1f
# 企业2的利润函数
profit2 = (12-(q1d+q2d)-t1)*q2d + (12-(q1f+q2f)-t2)*q2f

# 求解古诺均衡的一阶条件
dprofit1_d = diff(profit1, q1d)
dprofit1_f = diff(profit1, q1f)
dprofit2_d = diff(profit2, q2d)
dprofit2_f = diff(profit2, q2f)

# 由对称性，q1d=q2d, q1f=q2f
# 解方程组得到均衡产量
eq1 = dprofit1_d.subs([(q2d,q1d), (q2f,q1f)])
eq2 = dprofit1_f.subs([(q2d,q1d), (q2f,q1f)])

qd = solve(eq1, q1d)[0]  # 国内市场均衡产量
qf = solve(eq2, q1f)[0]  # 国际市场均衡产量

# 计算社会福利
Qd = 2*qd  # 国内市场总产量
Qf = 2*qf  # 国际市场总产量
CS = (12-Qd)*Qd/2  # 消费者剩余
PS = 2*((12-Qd-t1)*qd + (12-Qf-t2)*qf)  # 生产者剩余
TR = t1*Qd + t2*Qf  # 税收收入
W = CS + PS + TR  # 社会福利

# 求解最优税率
dW_t1 = diff(W, t1)
dW_t2 = diff(W, t2)
sol = solve([dW_t1, dW_t2], [t1, t2])

print("a) 分别征税的情况：")
print(f"最优内销税率t1 = {sol[t1]}")
print(f"最优出口税率t2 = {sol[t2]}\n")

# b) 单一税率的情况
t = symbols("t")  # 统一税率
# 重新计算均衡和社会福利
profit1_single = (12-(q1d+q2d)-t)*q1d + (12-(q1f+q2f)-t)*q1f
profit2_single = (12-(q1d+q2d)-t)*q2d + (12-(q1f+q2f)-t)*q2f

dprofit1_d_single = diff(profit1_single, q1d)
dprofit1_f_single = diff(profit1_single, q1f)

eq1_single = dprofit1_d_single.subs([(q2d,q1d), (q2f,q1f)])
eq2_single = dprofit1_f_single.subs([(q2d,q1d), (q2f,q1f)])

qd_single = solve(eq1_single, q1d)[0]
qf_single = solve(eq2_single, q1f)[0]

Qd_single = 2*qd_single
Qf_single = 2*qf_single
CS_single = (12-Qd_single)*Qd_single/2
PS_single = 2*((12-Qd_single-t)*qd_single + (12-Qf_single-t)*qf_single)
TR_single = t*(Qd_single + Qf_single)
W_single = CS_single + PS_single + TR_single

dW_single = diff(W_single, t)
t_opt = solve(dW_single, t)[0]

print("b) 单一税率的情况：")
print(f"最优税率t = {t_opt}")
