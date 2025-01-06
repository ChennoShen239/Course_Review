from sympy import symbols, solve, diff, simplify

# Define variables
P, t, A, B = symbols('P t A B')

# Define demand functions
Q_d = A - P  # domestic demand
Q_f = B - P  # foreign demand

# Define profit function
profit = (P - t)*(A - P) + P*(B - P)


# Find optimal price
dprofit_dP = diff(profit, P)
P_star = solve(dprofit_dP, P)[0]
print("\nOptimal price as function of t:")
print(f"P*(t) = {P_star}")

# Calculate quantities
Q_d_star = A - P_star
Q_f_star = B - P_star
print("\nOptimal quantities as functions of t:")
print(f"Q_d*(t) = {Q_d_star}")
print(f"Q_f*(t) = {Q_f_star}")

# Calculate welfare components
profit_star = profit.subs(P, P_star)
CS_star = (Q_d_star**2)/2  # consumer surplus
tax_revenue = t*Q_d_star
welfare = profit_star + CS_star + tax_revenue

# Find optimal tax rate
dwelfare_dt = diff(welfare, t)
t_star = solve(dwelfare_dt, t)[0]
print("\nOptimal tax rate:")
print(f"t* = {simplify(t_star)}")

# Verify results with numerical example
print("\nVerification with numerical example:")
# Choose values satisfying A < 3B and B < 3A
A_val, B_val = 10, 8
subs_dict = {A: A_val, B: B_val}

t_val = float(t_star.subs(subs_dict))
P_val = float(P_star.subs(t, t_val).subs(subs_dict))
Q_d_val = float(Q_d_star.subs(t, t_val).subs(subs_dict))
Q_f_val = float(Q_f_star.subs(t, t_val).subs(subs_dict))

print(f"\nFor A = {A_val}, B = {B_val}:")
print(f"Optimal tax rate t* = {t_val}")
print(f"Optimal price P* = {P_val}")
print(f"Domestic quantity Q_d* = {Q_d_val}")
print(f"Foreign quantity Q_f* = {Q_f_val}")

# Verify conditions
print("\nVerifying positive quantities:")
print(f"Q_d* > 0: {Q_d_val > 0}")
print(f"Q_f* > 0: {Q_f_val > 0}")
print(f"A < 3B: {A_val < 3*B_val}")
print(f"B < 3A: {B_val < 3*A_val}") 