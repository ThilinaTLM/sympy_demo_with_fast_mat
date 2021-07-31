# %%
from sympy import Symbol, Eq, factor, det, solve, init_printing
from sympy.abc import a, b, c, x, y, s, t
from sympy.matrices import zeros, ones, diag, MatrixSymbol
from sympy.matrices.expressions import dotproduct
import fast_mat as fast

init_printing(use_latex="mathjax")

L = Symbol('lambda')
I4 = fast.I(4)
I3 = fast.I(3)
I2 = fast.I(2)

print("INITIALIZED !")

# ========================================================================================================

# %%
A = fast.mat("""

""")
A


# %%
A.echelon_form()
# %%

-6 - 8*3 - 2 - 4
# %%
1 + 9 + 1 + 1
# %%

# %%
u1 = fast.mat("""
-1
3
1
1
""")

u2 = fast.mat("""
6
-8
-2
-4
""")

u3 = fast.mat("""
6
3
6
-3
""")
# %%
v1 = u1
v2 = u2 + (3)*v1
# %%
u3.dot(v2)
# %%
u3 - (30/12)*v2 - (6/12)*v1


# %%

A = fast.mat("""
2 4 -2
2 -1 -2
-4 -2 -5
""")
A

# %%
L*I3 - A
# %%
factor(det(L*I3 - A))

# %%
A - 5*I3

# %%
(A - 5*I3).echelon_form()
# %%
vals, X = fast.vector_var('x', 3)

# %%
solve(Eq((A+6*I3)*X, zeros(3, 1)), vals)

# %%
P = fast.mat("""
1/16 -2 -2
3/8 3 -1
1 1 1
""")
P

# %%
P.inv()
# %%
P.inv()*A*P
# %%
A = fast.mat("""
1 2
2 1
""")
A
# %%
det(L*I2-A)
