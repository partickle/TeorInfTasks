from math import log, ceil


def q_si(prob):
    res, tmp = [0], 0

    for i, val in enumerate(prob):
        tmp += val
        res.append(round(tmp, 13))
    res.pop(len(prob))

    return res


def g_sik(prob, s):
    res, tmp = [1], 1

    for i, val in enumerate(s):
        tmp *= prob[val - 1]
        res.append(round(tmp, 13))

    return res


def f_sik(s, q_si, g_sik):
    res, tmp = [0], 0

    for i, val in enumerate(s):
        tmp += q_si[val - 1] * g_sik[i]
        res.append(round(tmp, 13))

    return res


def float_to_binary(num):
    exponent = 0
    shifted_num = num
    while shifted_num != int(shifted_num):
        shifted_num *= 2
        exponent += 1
    if exponent == 0:
        return '{0:0b}'.format(int(shifted_num))
    binary = '{0:0{1}b}'.format(int(shifted_num), exponent + 1)
    integer_part = binary[:-exponent]
    fractional_part = binary[-exponent:].rstrip('0')
    return '{0}.{1}'.format(integer_part, fractional_part)


def decoding(q_si, f_sik, g_sik):
    res, tmp = [], 0

    for i in range(len(g_sik)):
        mini_res = []
        for j, val in enumerate(q_si):
            tmp = f_sik[i] + val * g_sik[i]
            mini_res.append(round(tmp, 13))
        res.append(mini_res)
    res.pop(len(g_sik) - 1)

    return res


def print_output(input):
    prob, s = input[0], input[1]

    print(' ======================= ВХОДНЫЕ ДАННЫЕ ======================== ')
    print(f'prob -> {prob}')
    print(f's -> {s}\n')

    print(' ======================== КОДИРОВАНИЕ ========================== ')

    q_si_ = q_si(prob)
    print(f'q_si -> {q_si_}')

    g_sik_ = g_sik(prob, s)
    print(f'g_sik -> {g_sik_}')

    f_sik_ = f_sik(s, q_si_, g_sik_)
    print(f'f_sik -> {f_sik_}\n')

    l = ceil(-log(g_sik_[len(g_sik_) - 1], 2)) + 1
    print(f'Длина кодового слова -> {l}')

    x = f_sik_[len(f_sik_) - 1] + g_sik_[len(g_sik_) - 1] / 2
    print(f'Кодовое слово в 10 сс -> {x}')

    bin_x = float_to_binary(x)[2:l + 2]
    print(f'Итоговое кодовое слово в 2 сс -> {bin_x}\n')

    print(' ======================= ДЕКОДИРОВАНИЕ ========================= ')

    decoding_ = decoding(q_si_, f_sik_, g_sik_)

    for i, val in enumerate(decoding_):
        print(f'k = {i + 1} -> {val}')

    print('\n\n')
