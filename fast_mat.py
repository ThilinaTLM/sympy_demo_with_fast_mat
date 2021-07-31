from sympy import Matrix, Symbol, pprint
from sympy.matrices import diag
from sympy.parsing.latex import parse_latex
from re import match, sub


def mat(text: str) -> Matrix:
    """
        Generate Matrix from string
    """
    lines = filter(lambda l: len(l.strip()) > 0, text.split('\n'))
    rows = list(map(
        lambda l: list(map(parse_latex, l.strip().split())),
        lines
    ))
    mat = Matrix(rows)
    mat.simplify()
    return mat


def I(n):
    """
    Generate Identity Vector
    """
    return diag([1]*n, unpack=True)


def vector_var(name: str, rows: int):
    """
    Generate variable vector with variables
    """
    syms = [Symbol(f'{name}{i}') for i in range(1, rows+1)]
    return (tuple(syms), Matrix(syms))


def row_op(mat: Matrix, row_to: int, row_do: int, factor=1) -> Matrix:
    """
    Single row operation
    """
    m = mat
    m.row_op(row_to, lambda v, i: v + factor*m[row_do, i])
    return m


def find_pivot_row(mat: Matrix, column_num: int) -> int:
    """
    Find row number of pivot row
    """
    column = mat[:, column_num]
    for i in range(column_num, mat.shape[0]):
        if column[i] != 0:
            return i
    return -1


def row_echelon(mat: Matrix) -> Matrix:
    """
    Step by Step row operations for row echelon form
    """
    m = mat.copy()
    steps = min(*m.shape)-1
    r = 0
    while r < steps:
        pivot_row = find_pivot_row(m, r)
        if (pivot_row == r):
            pivot_value = m[pivot_row, pivot_row]
            nothing_done = True
            for i in range(r+1, m.shape[0]):
                factor = -1*(m[i, r]/pivot_value)
                if factor == 0:
                    continue
                print(f"R{i + 1} = R{i + 1} + ({factor})R{r + 1}")
                row_op(m, i, r, factor)
                nothing_done = False
            if not nothing_done:
                pprint(m)
            r += 1
        elif (pivot_row > r):
            print(f"R{pivot_row + 1} <-> R{r + 1}")
            m.row_swap(pivot_row, r)
            pprint(m)
        else:
            r += 1
            continue

        print()
    return m


def row_op_interactive(mat, globals={}):
    """
    Interactive row operations
    """
    clone = mat.copy()
    while True:
        inp = input("OP$ ").replace(' ', '')
        if inp == "":
            break
        if match(r"\d=.+", inp):
            row = int(inp[0])-1
            _, op = inp.split('=')
            clone.row_op(
                row,
                lambda v, i: eval(
                    sub(r'r(\d)', r'm[\1-1, i]', op),
                    globals, {'m': clone, 'i': i, 'v': v}
                )
            )
            pprint(clone)
        elif match(r"\d,\d", inp):
            r1, r2 = map(int, inp.split(','))
            clone.row_swap(r1-1, r2-1)
            pprint(clone)
        else:
            print("Invalid")
            pprint(clone)
    return clone

