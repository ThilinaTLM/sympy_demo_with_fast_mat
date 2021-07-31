from sympy import *
from sympy.abc import x,y,z,s,t,a,b,c
from sympy.parsing.latex import parse_latex
from re import split, match, sub

init_printing(use_unicode=True)

def fast_mat():
    rows = []
    row_number = 0
    while True:
        inp = input(f"R{row_number}$ ").strip()
        if inp == "":
            break
        values = split(r"(?:[ ,]+)", inp)
        rows.append(list(map(parse_latex, values)))
        row_number += 1
    return Matrix(rows)


def fast_row_operation(mat, globals = {}):
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
                lambda v,i: eval(sub(r'r(\d)', r'm[\1-1, i]', op), globals, {'m': clone, 'i': i, 'v': v})
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

