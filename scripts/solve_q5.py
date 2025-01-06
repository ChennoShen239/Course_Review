from sympy import symbols, solve, diff

# 定义变量
s1, s2 = symbols('s1 s2')  # 合并前的市场份额
p1, p2 = symbols('p1 p2')  # 合并前的价格
q1, q2 = symbols('q1 q2')  # 合并前的产量
pm = symbols('pm')         # 合并后的价格
qm = symbols('qm')        # 合并后的产量

# 定义需求函数（线性需求）
# P = a - bQ
a, b = 100, 1  # 需求参数
c = 20         # 边际成本

# 合并前的市场均衡
# 假设两个企业进行Cournot竞争
def pre_merger_equilibrium():
    # 利润函数
    pi1 = (a - b*(q1 + q2) - c)*q1
    pi2 = (a - b*(q1 + q2) - c)*q2
    
    # 一阶条件
    dpi1_dq1 = diff(pi1, q1)
    dpi2_dq2 = diff(pi2, q2)
    
    # 求解均衡产量
    solution = solve([dpi1_dq1, dpi2_dq2], [q1, q2])
    
    # 计算均衡价格和市场份额
    Q = solution[q1] + solution[q2]
    P = a - b*Q
    s1_val = solution[q1]/Q
    s2_val = solution[q2]/Q
    
    return solution[q1], solution[q2], P, s1_val, s2_val

# 合并后的市场均衡
def post_merger_equilibrium():
    # 合并后的利润函数
    pi_m = (a - b*qm - c)*qm
    
    # 一阶条件
    dpi_m_dqm = diff(pi_m, qm)
    
    # 求解均衡产量
    solution = solve(dpi_m_dqm, qm)
    
    # 计算均衡价格
    P = a - b*solution[0]
    
    return solution[0], P

# 计算结果
q1_pre, q2_pre, p_pre, s1_pre, s2_pre = pre_merger_equilibrium()
qm_post, pm_post = post_merger_equilibrium()

print("合并前：")
print(f"企业1产量: {q1_pre}")
print(f"企业2产量: {q2_pre}")
print(f"市场价格: {p_pre}")
print(f"企业1市场份额: {s1_pre}")
print(f"企业2市场份额: {s2_pre}")

print("\n合并后：")
print(f"合并企业产量: {qm_post}")
print(f"市场价格: {pm_post}")

# 计算反垄断部门预测的市场份额和实际市场份额的差异
predicted_share = s1_pre + s2_pre
actual_share = 1.0  # 合并后企业占据整个市场

print("\n市场份额分析：")
print(f"反垄断部门预测的市场份额: {predicted_share}")
print(f"实际市场份额: {actual_share}")
print(f"预测误差: {actual_share - predicted_share}")

# 计算消费者剩余变化
def consumer_surplus(p, q):
    return 0.5*(a - p)*q

cs_pre = consumer_surplus(p_pre, q1_pre + q2_pre)
cs_post = consumer_surplus(pm_post, qm_post)

print("\n福利分析：")
print(f"合并前消费者剩余: {cs_pre}")
print(f"合并后消费者剩余: {cs_post}")
print(f"消费者剩余变化: {cs_post - cs_pre}") 