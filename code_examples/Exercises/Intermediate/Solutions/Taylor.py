import sympy as sp
import matplotlib.pyplot as plt
import numpy as np

""" 
Takes as input:
  f: the function to approximate.
  a: the expansion point.
  n: the order of the polynomial.
  x: the symbolic variable from SymPy.
"""


def taylor_polynomial(f, a, n, x):
    """
    Computes the Taylor polynomial of order n for function f around point a.
    """
    Pn = 0
    for k in range(n + 1):
        deriv = sp.diff(f, x, k)  # k-th derivative
        deriv_at_a = deriv.subs(x, a)  # evaluate at a
        term = (deriv_at_a / sp.factorial(k)) * (x - a) ** k
        Pn += term
    return sp.simplify(Pn)


# Define symbolic variable and function
x = sp.Symbol("x")
f = sp.sin(x)

# Taylor polynomial around 0, order 5
Pn = taylor_polynomial(f, 0, 5, x)
print("Taylor Polynomial:", Pn)

# Convert to numerical functions
f_lamb = sp.lambdify(x, f, "numpy")
Pn_lamb = sp.lambdify(x, Pn, "numpy")

# Plot
X = np.linspace(-2 * np.pi, 2 * np.pi, 400)
plt.plot(X, f_lamb(X), label="f(x) = sin(x)")
plt.plot(X, Pn_lamb(X), label="Taylor Polynomial (n=5)")
plt.legend()
plt.grid(True)
plt.show()
