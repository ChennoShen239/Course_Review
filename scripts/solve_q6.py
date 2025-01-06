from sympy import symbols, solve, diff

# 定义变量
p1, p2 = symbols('p1 p2')  # 独立企业的价格
pm = symbols('pm')         # 合并后的价格

# 市场参数
a = 20  # 需求曲线截距
b = 1   # 需求曲线斜率
c = 0   # 边际成本

# 独立企业的情况
def independent_firms():
    # 需求函数
    q1 = a - b*p1 + 0.5*b*p2
    q2 = a - b*p2 + 0.5*b*p1
    
    # 利润函数
    pi1 = (p1 - c)*q1
    pi2 = (p2 - c)*q2
    
    # 一阶条件
    dpi1_dp1 = diff(pi1, p1)
    dpi2_dp2 = diff(pi2, p2)
    
    # 求解均衡价格
    solution = solve([dpi1_dp1, dpi2_dp2], [p1, p2])
    
    # 计算均衡产量和利润
    q1_eq = q1.subs([(p1, solution[p1]), (p2, solution[p2])])
    q2_eq = q2.subs([(p1, solution[p1]), (p2, solution[p2])])
    pi1_eq = pi1.subs([(p1, solution[p1]), (p2, solution[p2])])
    pi2_eq = pi2.subs([(p1, solution[p1]), (p2, solution[p2])])
    
    return solution[p1], solution[p2], q1_eq, q2_eq, pi1_eq, pi2_eq

# 合并后的情况
def merged_firm():
    # 需求函数
    q1 = a - b*pm + 0.5*b*pm
    q2 = a - b*pm + 0.5*b*pm
    
    # 总利润函数
    pi_m = (pm - c)*(q1 + q2)
    
    # 一阶条件
    dpi_m_dpm = diff(pi_m, pm)
    
    # 求解均衡价格
    solution = solve(dpi_m_dpm, pm)
    
    # 计算均衡产量和利润
    q_total = (q1 + q2).subs(pm, solution[0])
    pi_total = pi_m.subs(pm, solution[0])
    
    return solution[0], q_total, pi_total

# 计算结果
p1_ind, p2_ind, q1_ind, q2_ind, pi1_ind, pi2_ind = independent_firms()
pm_merged, qm_merged, pim_merged = merged_firm()

print("独立企业情况：")
print(f"企业1价格: {p1_ind}")
print(f"企业2价格: {p2_ind}")
print(f"企业1产量: {q1_ind}")
print(f"企业2产量: {q2_ind}")
print(f"企业1利润: {pi1_ind}")
print(f"企业2利润: {pi2_ind}")

print("\n合并后情况：")
print(f"价格: {pm_merged}")
print(f"总产量: {qm_merged}")
print(f"总利润: {pim_merged}")

# 计算消费者剩余变化
def consumer_surplus(p, q):
    return 0.5*(a - p)*q

cs_ind = consumer_surplus(p1_ind, q1_ind + q2_ind)
cs_merged = consumer_surplus(pm_merged, qm_merged)

print("\n福利分析：")
print(f"合并前消费者剩余: {cs_ind}")
print(f"合并后消费者剩余: {cs_merged}")
print(f"消费者剩余变化: {cs_merged - cs_ind}")

# 分析价格协议的反垄断含义
print("\n反垄断含义：")
print(f"价格上涨幅度: {(pm_merged - p1_ind)/p1_ind * 100}%")
print("价格协议模拟了合并的效果，但没有效率改进的好处") 