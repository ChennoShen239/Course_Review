from sympy import symbols, expand, simplify

# 定义符号变量
t1 = symbols('t1')

# 计算均衡数量和价格
Q = 2*(12-t1)/3
P = 12 - Q - t1

# 消费者剩余计算
CS = (1/2)*Q*(12-Q-t1)

print("修正后的消费者剩余:")
print(expand(CS)) 