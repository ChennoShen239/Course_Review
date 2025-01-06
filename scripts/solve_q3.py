from sympy import symbols, solve, diff, simplify

# Define variables
L, q, gamma, z = symbols('L q gamma z')
c_L, c_q = symbols('c_L c_q')  # partial derivatives of cost function

# Revenue function using geometric series formula
# Sum of geometric series: (1-r^n)/(1-r) where r is the common ratio
# Here r = q*gamma
revenue = (1 - (q*gamma)**L)/(1 - q*gamma) + z*gamma**L

# First order conditions
# 1. FOC with respect to L
foc_L = diff(revenue, L) - c_L
# 2. FOC with respect to q
foc_q = diff(revenue, q) - c_q

print("First order conditions:")
print("\nFOC with respect to L:")
print(simplify(foc_L))
print("\nFOC with respect to q:")
print(simplify(foc_q))

# Substitute some specific values to get a numerical solution
# Let's try gamma = 0.9, z = 0.1
# And assume linear marginal costs: c_L = 0.1, c_q = 0.1
subs_dict = {
    gamma: 0.9,
    z: 0.1,
    c_L: 0.1,
    c_q: 0.1
}

# Try to solve the system for some reasonable initial values
foc_L_subs = foc_L.subs(subs_dict)
foc_q_subs = foc_q.subs(subs_dict)

print("\nTrying to solve with specific values:")
print("gamma = 0.9, z = 0.1, c_L = 0.1, c_q = 0.1")

# Solve numerically for L and q
solution = solve([foc_L_subs, foc_q_subs], [L, q])

print("\nSolutions:")
for sol in solution:
    L_val, q_val = sol
    # Check if solution is real and in reasonable range
    if L_val.is_real and q_val.is_real and 0 < q_val < 1 and L_val > 0:
        print(f"L = {L_val.evalf()}")
        print(f"q = {q_val.evalf()}")
        
        # Calculate revenue and verify zero profit condition
        rev = revenue.subs({L: L_val, q: q_val, gamma: 0.9, z: 0.1})
        print(f"Revenue = {rev.evalf()}")
        print("This should approximately equal total cost for zero profit condition") 