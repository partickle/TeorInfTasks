from math import log

from sympy import symbols, Eq, solve

from task1 import entropy


# ================== РЕШЕНИЕ СЛАУ ================== #


def find_sle(matrix):
    if len(matrix) == 3:
        return find_sle_for_3(matrix)

    return find_sle_for_4(matrix)


def find_sle_for_3(matrix):
    a, b, c = symbols('a b c')

    eq1 = Eq(a - matrix[0][0] * a - matrix[0][1] * b - matrix[0][2] * c, 0)
    eq2 = Eq(b - matrix[1][0] * a - matrix[1][1] * b - matrix[1][2] * c, 0)
    eq3 = Eq(c - matrix[2][0] * a - matrix[2][1] * b - matrix[2][2] * c, 0)
    eq4 = Eq(a + b + c, 1)

    solution = solve((eq1, eq2, eq3, eq4), (a, b, c))

    return [solution[a], solution[b], solution[c]]


def find_sle_for_4(matrix):
    a, b, c, d = symbols('a b c d')

    eq1 = Eq(a - matrix[0][0] * a - matrix[0][1] * b - matrix[0][2] * c - matrix[0][3] * d, 0)
    eq2 = Eq(b - matrix[1][0] * a - matrix[1][1] * b - matrix[1][2] * c - matrix[1][3] * d, 0)
    eq3 = Eq(c - matrix[2][0] * a - matrix[2][1] * b - matrix[2][2] * c - matrix[2][3] * d, 0)
    eq4 = Eq(c - matrix[3][0] * a - matrix[3][1] * b - matrix[3][2] * c - matrix[3][3] * d, 0)
    eq5 = Eq(a + b + c, 1)

    solution = solve((eq1, eq2, eq3, eq4, eq5), (a, b, c, d))

    return [solution[a], solution[b], solution[c], solution[d]]


# ================ ВЫВОД ================ #


def print_output(matrix):
    probs = find_sle(matrix)
    ent = entropy.inf_bin_entropy(probs)
    joint_probs = entropy.joint_probs(probs, matrix)
    joint_entropy = entropy.joint_entropy_ans_arr(joint_probs)

    dig_word = {0: 'a', 1: 'b', 2: 'c', 3: 'd'}

    print(' ======================= ВХОДНЫЕ ДАННЫЕ ======================== ')

    for i, arr in enumerate(matrix):
        for j, val in enumerate(arr):
            print(f'P({dig_word[i]}|{dig_word[j]}) = {val}', end=' ')
        print()

    print()

    print(' =========== Вероятности стационарного распределения =========== ')

    for i, val in enumerate(probs):
        print(f'P{dig_word[i]} = {round(val, 3)}')

    print()

    print(' ========================== Энтропия =========================== ')

    print(f'H(Xi) = {round(ent, 3)}')

    print()

    print(' =================== Совместные вероятности ==================== ')

    for i, arr in enumerate(joint_probs):
        for j, val in enumerate(arr):
            print(f'P(Xi = {dig_word[j]}, Xi+1 = {dig_word[i]}) = {round(val, 3)}')

    print()

    print(' ===================== Совместная энтропия ===================== ')

    print(f'H(XiXi+1) = {round(joint_entropy, 3)}')

    print()

    print(' ===================== Совместная энтропия ===================== ')

    print(f'HXi(Xi+1) = {round(joint_entropy - ent, 3)}')

    print('\n\n')
