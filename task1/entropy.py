from task1 import ensembles
from math import log


# ================== ИНФОРМАЦИОННАЯ ДВОИЧНАЯ ЭНТРОПИЯ ================== #


# Функция, которая считает энтропию для одного ансамбля
def inf_bin_entropy(p_arr):
    h = 0
    for i, val in enumerate(p_arr):
        h -= val * log(val, 2)
    return h


# Подсчет энтропии для двух ансамблей, первый - H(X), второй - H(Y)
def inf_bin_ent_p_arr(p_arr):
    h_ans_arr = []
    for i in range(len(p_arr)):
        h_ans_arr.append(
            inf_bin_entropy(p_arr[i])
        )
    return h_ans_arr


# Подсчет энтропии для двух ансамблей, если известно их произведение
def inf_bin_ent_ans_arr(ans_arr):
    return inf_bin_ent_p_arr(ensembles.create_p_arr(ans_arr))


# ================== СОВМЕСТНАЯ ЭНТРОПИЯ ================== #


# Функция нахождения совместной энтропии из произведения ансамблей
def joint_probs(probs, cond_prob):
    res = []

    for i, arr in enumerate(cond_prob):
        res.append([])
        for j, val in enumerate(arr):
            res[i].append(probs[j]*val)

    return res


def joint_entropy_cond_prob():
    pass


# Функция подсчета совместной энтропии из произведения ансамблей
def joint_entropy_ans_arr(ans_arr):
    h_xy = 0
    for i in range(len(ans_arr)):
        for j, val in enumerate(ans_arr[i]):
            h_xy -= val * log(val, 2)
    return h_xy


# ================== ПОЛНАЯ УСЛОВНАЯ ЭНТРОПИЯ ================== #


# Функция для подсчета частичной условной энтропии
def private_cond_entropy(cond_p_arr):
    res = []

    for j, val in enumerate(cond_p_arr[0]):
        temp = 0

        for i, arr in enumerate(cond_p_arr):
            temp -= cond_p_arr[i][j] * log(cond_p_arr[i][j], 2)

        res.append(temp)

    return res


# Функция для подсчета частичной условной энтропии через начальное условие
def private_cond_entropy_ans_arr(ans_arr):
    return [private_cond_entropy(ensembles.calc_cond_prob_y(ans_arr)),
            private_cond_entropy(ensembles.calc_cond_prob_x(ans_arr))]


# Функция для подсчета полной условной энтропии
def total_cond_entropy(ans_arr):
    return [(joint_entropy_ans_arr(ans_arr) - inf_bin_ent_ans_arr(ans_arr)[0]),
            (joint_entropy_ans_arr(ans_arr) - inf_bin_ent_ans_arr(ans_arr)[1])]


# ================== ВЫВОД ================== #

def print_output(ans_arr):
    print(' =============== Энтропия ансамблей =============== ')
    print(f'H(X): {round(inf_bin_ent_ans_arr(ans_arr)[0], 3)}, '
          f'H(Y): {round(inf_bin_ent_ans_arr(ans_arr)[1], 3)}, \n')

    print(' ========== Совместная энтропия ансамблей ========= ')
    print(f'H(XY): {round(joint_entropy_ans_arr(ans_arr), 3)}, \n')

    print(' ========== Совместная энтропия ансамблей ========= ')

    for i, val in enumerate(private_cond_entropy_ans_arr(ans_arr)[0]):
        print(f'Hx{i + 1}(Y) = {round(val, 3)}', end=', ')
    print()

    for i, val in enumerate(private_cond_entropy_ans_arr(ans_arr)[1]):
        print(f'Hy{i + 1}(X) = {round(val, 3)}', end=', ')
    print('\n')

    print(' ============ Полные условные энтропии ============ ')
    print(f'Hx(Y): {round(total_cond_entropy(ans_arr)[0], 3)}, '
          f'Hy(X): {round(total_cond_entropy(ans_arr)[1], 3 )}')
    print('\n')
