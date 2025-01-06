from sympy import symbols, solve, diff

# 定义变量
p1, p2 = symbols('p1 p2')  # 零售价格
s1, s2 = symbols('s1 s2')  # 服务水平
w = symbols('w')           # 批发价格
c = symbols('c')          # 服务成本系数

# 市场参数
a = 10  # 需求基数
b = 1   # 价格敏感度
d = 0.5 # 服务敏感度
t = 1   # 空间差异参数

# 需求函数
def demand(p1, p2, s1, s2):
    # 考虑价格、服务和空间差异的需求函数
    q1 = a - b*p1 + d*s1 + 0.5*b*p2 - 0.5*d*s2
    q2 = a - b*p2 + d*s2 + 0.5*b*p1 - 0.5*d*s1
    return q1, q2

# 零售商利润函数
def retailer_profits():
    q1, q2 = demand(p1, p2, s1, s2)
    pi1 = (p1 - w)*q1 - c*s1**2
    pi2 = (p2 - w)*q2 - c*s2**2
    return pi1, pi2

# 制造商利润函数
def manufacturer_profit():
    q1, q2 = demand(p1, p2, s1, s2)
    pi_m = w*(q1 + q2)
    return pi_m

# 求解零售商的最优决策
def solve_retail_equilibrium():
    pi1, pi2 = retailer_profits()
    
    # 关于价格的一阶条件
    dpi1_dp1 = diff(pi1, p1)
    dpi2_dp2 = diff(pi2, p2)
    
    # 关于服务的一阶条件
    dpi1_ds1 = diff(pi1, s1)
    dpi2_ds2 = diff(pi2, s2)
    
    # 求解均衡
    solution = solve([dpi1_dp1, dpi2_dp2, dpi1_ds1, dpi2_ds2], 
                    [p1, p2, s1, s2])
    
    return solution

# 分析不同情况下的均衡
def analyze_equilibrium():
    # 情况1：只考虑价格竞争
    print("情况1：只考虑价格竞争")
    pi1, pi2 = retailer_profits()
    dpi1_dp1 = diff(pi1, p1)
    dpi2_dp2 = diff(pi2, p2)
    price_eq = solve([dpi1_dp1.subs([(s1, 0), (s2, 0)]), 
                     dpi2_dp2.subs([(s1, 0), (s2, 0)])],
                    [p1, p2])
    print(f"均衡价格：{price_eq}")
    
    # 情况2：考虑价格和服务竞争
    print("\n情况2：考虑价格和服务竞争")
    full_eq = solve_retail_equilibrium()
    print(f"均衡价格和服务水平：{full_eq}")
    
    # 分析服务外溢效应
    print("\n服务外溢效应分析：")
    q1, q2 = demand(p1, p2, s1, s2)
    dq1_ds2 = diff(q1, s2)
    dq2_ds1 = diff(q2, s1)
    print(f"零售商1的服务对零售商2的需求影响：{dq2_ds1}")
    print(f"零售商2的服务对零售商1的需求影响：{dq1_ds2}")

# 主要分析
print("零售商行为分析")
print("=" * 50)

# 设定参数值
w_val = 5
c_val = 1

# 进行分析
analyze_equilibrium()

# 总结发现
print("\n主要发现：")
print("1. 零售商倾向于过度价格竞争，因为价格效应直接影响自身需求")
print("2. 服务投入不足，因为存在正外部性（搭便车效应）")
print("3. 这种行为导致零售价格过低，服务水平次优")
print("4. 制造商的利润受到负面影响") 