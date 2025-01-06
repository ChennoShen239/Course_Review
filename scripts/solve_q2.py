from sympy import symbols, solve, diff, simplify

def calculate_welfare(c1, c2):
    # Calculate quantities
    q1 = (12 + c2 - 2*c1)/3
    q2 = (12 + c1 - 2*c2)/3
    Q = q1 + q2
    
    # Calculate price
    P = 12 - Q
    
    # Calculate profits
    pi1 = (P - c1)*q1
    pi2 = (P - c2)*q2
    
    # Calculate consumer surplus
    CS = Q**2/2
    
    # Calculate total welfare
    W = CS + pi1 + pi2
    
    return {
        'q1': q1,
        'q2': q2,
        'Q': Q,
        'P': P,
        'pi1': pi1,
        'pi2': pi2,
        'CS': CS,
        'W': W
    }

# Initial state: c1 = c2 = 6
print("\nInitial state (c1 = c2 = 6):")
initial = calculate_welfare(6, 6)
for key, value in initial.items():
    print(f"{key} = {value}")

# After innovation: c1 = 3, c2 = 6
print("\nAfter innovation (c1 = 3, c2 = 6):")
after = calculate_welfare(3, 6)
for key, value in after.items():
    print(f"{key} = {value}")

# Calculate welfare change
welfare_change = after['W'] - initial['W']
print(f"\nWelfare change: {welfare_change}")

# Calculate profit change for firm 1
profit_change = after['pi1'] - initial['pi1']
print(f"Profit change for firm 1: {profit_change}")

print("\nTherefore, if K < {profit_change}, firm 1 will invest,")
print(f"and if K < {welfare_change}, the investment increases social welfare.") 