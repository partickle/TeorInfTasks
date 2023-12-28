from math import log, ceil


def q_i(prob):
    res, tmp = [0], 0

    for i, val in enumerate(prob):
        tmp += val
        res.append(round(tmp, 8))
    res.pop(len(prob))

    return res


def delta_i(prob, q_i):
    res = []

    for i in range(len(prob)):
        val = q_i[i] + prob[i] / 2
        res.append(round(val, 8))

    return res


def l_i(prob):
    res = []

    for i, val in enumerate(prob):
        val = -log(val, 2) + 1
        res.append(ceil(val))

    return res


def bin_delta_i(delta_i):
    res = []

    for i, val in enumerate(delta_i):
        res.append(decimal_to_binary(val))

    return res

def bin_code(delta_i, l_i):
    res = []

    for i, val in enumerate(delta_i):
        tmp = val[2:]
        res.append(tmp[:l_i[i]])

    return res


def entropy(prob):
    res = 0

    for i, val in enumerate(prob):
        res -= val * log(val, 2)

    return res


def length_code(prob, l_i):
    res = 0

    for i, val in enumerate(prob):
        res += val * l_i[i]

    return res


def decimal_to_binary(num):
    if num < 0:
        return "Только положительные числа"

    integer_part = int(num)
    binary_integer_part = bin(integer_part).replace('0b', '')

    fractional_part = num - integer_part
    binary_fractional_part = ''

    while fractional_part:
        fractional_part *= 2
        bit = int(fractional_part)
        if bit == 1:
            fractional_part -= bit
            binary_fractional_part += '1'
        else:
            binary_fractional_part += '0'

        if len(binary_fractional_part) > 10:
            break

    return binary_integer_part + '.' + binary_fractional_part if binary_fractional_part else binary_integer_part


def print_output(prob):
    print(' ======================= ВХОДНЫЕ ДАННЫЕ ======================== ')
    print(f'{prob}\n')

    print(' ========================== ТАБЛИЦА ============================ ')

    q_i_ = q_i(prob)
    print(f'q_i -> {q_i_}')

    delta_i_ = delta_i(prob, q_i_)
    print(f'delta_i -> {delta_i_}')

    l_i_ = l_i(prob)
    print(f'l_i -> {l_i_}')

    bin_delta_i_ = bin_delta_i(delta_i_)
    print(f'bin_delta_i -> {bin_delta_i_}')

    bin_code_ = bin_code(bin_delta_i_, l_i_)
    print(f'bin_code -> {bin_code_}\n')

    print(' ====================== ЭНТРОПИЯ И Т.Д. ======================== ')

    length_code_ = length_code(prob, l_i_)
    print(f'Длинна кода -> {length_code_}')

    entropy_ = entropy(prob)
    print(f'Энтропия -> {entropy_}')

    print(f'Избыточность -> {length_code_ - entropy_}\n')
