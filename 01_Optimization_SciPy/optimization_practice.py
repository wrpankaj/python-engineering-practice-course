from scipy.optimize import linprog, minimize

# -----------------------------
# Task 1: Linear Programming
# -----------------------------

# Maximize Z = 45x1 + 80x2
# scipy linprog solves minimization, therefore use negative coefficients

c = [-45, -80]

A = [
    [5, 20],
    [10, 15]
]

b = [400, 450]

bounds = [(0, None), (0, None)]

result = linprog(c, A_ub=A, b_ub=b, bounds=bounds, method="highs")

print("Optimization Problem: Furniture Manufacturing")

if result.success:
    print("Number of Chairs =", result.x[0])
    print("Number of Tables =", result.x[1])
    print("Maximum Profit = Rs.", -result.fun)
else:
    print("No solution found")

# -----------------------------
# Task 2: Unconstrained Optimization
# -----------------------------

def f(x):
    return x**2 + 3*x + 2

result2 = minimize(f, x0=0)

print("\nUnconstrained Optimization")
print("Optimal x =", result2.x[0])
print("Minimum value =", result2.fun)
