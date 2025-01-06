from sympy import symbols, solve, diff, simplify

# Define variables
p1, p2, lambda_var = symbols('p1 p2 lambda')

# Consumer surplus from buying bundle
CS = (1-p1)**2/2 + (1-p2)**2/2

# Consumer surplus from only buying product 2 at competitive price p2=0
CS_outside = 1/2

# Profit function
profit = p1*(1-p1) + p2*(1-p2)

# Lagrangian function
L = profit + lambda_var*(CS - CS_outside)


# First order conditions

foc_p1 = diff(L, p1)
foc_p2 = diff(L, p2)
foc_lambda = CS - CS_outside

# Solve the system of equations
solution = solve([foc_p1, foc_p2, foc_lambda], [p1, p2, lambda_var])

print("Solutions found:")
for sol in solution:
    p1_val, p2_val, lambda_val = sol
    print(f"\np1 = {p1_val}")
    print(f"p2 = {p2_val}")
    print(f"lambda = {lambda_val}")
    
    # Verify this is a valid solution
    if not all(x.is_real for x in [p1_val, p2_val, lambda_val]):
        print("Not a valid solution (complex numbers)")
        continue
        
    # Calculate consumer surplus and profit
    cs_val = CS.subs([(p1, p1_val), (p2, p2_val)])
    profit_val = profit.subs([(p1, p1_val), (p2, p2_val)])
    
    print(f"Consumer surplus = {cs_val}")
    print(f"Profit = {profit_val}")
    
    # Check second order conditions
    # TODO: Add check for second order conditions 