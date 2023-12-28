import math

from multipledispatch import dispatch


# ================== ВЕРОЯТНОСТЬ ================== #

# Функция нахождения вероятностей ансамбля X
def found_p_x(ans_arr, i_x):
    px = 0
    for i_y in range(len(ans_arr[0])):
        px += ans_arr[i_x][i_y]
    return px


# Функция нахождения вероятностей ансамбля Y
def found_p_y(ans_arr, i_y):
    py = 0
    for i_x in range(len(ans_arr)):
        py += ans_arr[i_x][i_y]
    return py


# Функция, которая создает массив ансамблей: первый - X, второй - Y
def create_p_arr(ans_arr):
    p_arr = [[], []]

    for i_x in range(len(ans_arr)):
        p_arr[0].append(found_p_x(ans_arr, i_x))

    for i_y in range(len(ans_arr[0])):
        p_arr[1].append(found_p_y(ans_arr, i_y))

    return p_arr


# ================== НЕЗАВИСИМОСТЬ ================== #

# Функция подсчета произведения вероятностей
@dispatch(list, list)
def calc_products(ans_arr, p_arr):
    res = []
    for i_x in range(len(ans_arr)):
        res.append([])
        for i_y, val in enumerate(ans_arr[i_x]):
            res[i_x].append(p_arr[0][i_x] * p_arr[1][i_y])
    return res


@dispatch(list)
def calc_products(ans_arr):
    return calc_products(ans_arr, create_p_arr(ans_arr))


# Функция, которая проверяет независимость ансамблей
@dispatch(list, list)
def check_independence(ans_arr, p_arr):
    for i_x in range(len(ans_arr)):
        for i_y, val in enumerate(ans_arr[i_x]):
            if not math.isclose(val, p_arr[0][i_x] * p_arr[1][i_y]):
                return False
    return True


@dispatch(list)
def check_independence(ans_arr):
    return check_independence(ans_arr, create_p_arr(ans_arr))


# ================== УСЛОВНЫЕ ВЕРОЯТНОСТИ ================== #


# Функция, которая считает условные вероятности
# для всех вероятностей ансамбля X
@dispatch(list, list)
def calc_cond_prob_x(ans_arr, p_arr):
    c_p_arr_x = []
    for i_x in range(len(ans_arr)):
        c_p_arr_x.append([])
        for i_y, val in enumerate(ans_arr[i_x]):
            c_p_arr_x[i_x].append(val/p_arr[1][i_y])
    return c_p_arr_x


@dispatch(list)
def calc_cond_prob_x(ans_arr):
    return calc_cond_prob_x(ans_arr, create_p_arr(ans_arr))


# Аналогично, но для ансамбля Y
# (транспонируем матрицу для удобства эксплуатации)
@dispatch(list, list)
def calc_cond_prob_y(ans_arr, p_arr):
    c_p_arr_y = []
    ans_arr = list(map(list, zip(*ans_arr)))
    for i_y in range(len(ans_arr)):
        c_p_arr_y.append([])
        for i_x, val in enumerate(ans_arr[i_y]):
            c_p_arr_y[i_y].append(val/p_arr[0][i_x])
    return c_p_arr_y


@dispatch(list)
def calc_cond_prob_y(ans_arr):
    return calc_cond_prob_y(ans_arr, create_p_arr(ans_arr))


# ================== ВЫВОД ================== #

def print_output(ans_arr):
    print(' ================== Вероятности: ================== ')

    for i, arr in enumerate(create_p_arr(ans_arr)):
        for j, val in enumerate(arr):
            print(f'p({"x" if i == 0 else "y"}{j + 1}) = {round(val, 3)}',
                  end=', ')
        print()
    print()

    print(' =========== Произведение вероятностей: =========== ')

    for i, arr in enumerate(calc_products(ans_arr)):
        for j, val in enumerate(arr):
            print(f'p(x{i + 1} * y{j + 1}) = {round(val, 3)}', end=', ')
        print()
    print()

    print(' ============= Ансамбли независимы?  ============== ')
    print(f'{check_independence(ans_arr)}\n')

    print(' ============== Условные вероятности ============== ')

    for i, arr in enumerate(calc_cond_prob_x(ans_arr)):
        for j, val in enumerate(arr):
            print(f'p(x{i + 1}|y{j + 1}) = {round(val, 3)}', end=', ')
        print()
    print()

    for i, arr in enumerate(calc_cond_prob_y(ans_arr)):
        for j, val in enumerate(arr):
            print(f'p(y{i + 1}|x{j + 1}) = {round(val, 3)}', end=', ')
        print()
    print()
