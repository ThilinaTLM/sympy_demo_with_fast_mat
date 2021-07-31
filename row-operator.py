import re
from sympy.parsing.latex import parse_latex
from sympy import Matrix, pprint_use_unicode, pprint
import math

def console_input_matrix():
    rows = []
    row_number = 1
    while True:
        inp = input(f"R{row_number}$ ").strip()
        if inp == "":
            break
        values = re.split(r'[ ,](?=[A-Za-z0-9]+\b)', inp)
        rows.append(list(map(parse_latex, values)))
        row_number += 1
    return Matrix(rows)


def main():
    mat = console_input_matrix()

    # show matrix
    print()
    print("INPUT: ")
    pprint(mat)

    # echelon form
    print()
    print("ECHELON FORM: ")
    pprint(mat.rref()[0])

if __name__ == '__main__':
    pprint_use_unicode()
    main()
    


