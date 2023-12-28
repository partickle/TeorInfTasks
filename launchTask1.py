from task1 import ensembles, entropy

# Входной массив представляет собой матрицу, в которая коррелирует с
# индексами элементов ансамбля, так x2y1 - это input_ans[2][1]
input_ans_1 = [[0.056, 0.055, 0.048, 0.067], [0.087, 0.061, 0.043, 0.066], [0.074, 0.056, 0.256, 0.131]]
input_ans_2 = [[0.049, 0.042, 0.074, 0.063], [0.082, 0.043, 0.111, 0.03], [0.053, 0.078, 0.343, 0.032]]


def print_task1(input_ans):
    print(' ================= ВХОДНЫЕ ДАННЫЕ: ================ ')
    for i, arr in enumerate(input_ans):
        for j, val in enumerate(arr):
            print(f'x{i + 1}y{j + 1} = {val}', end=', ')
        print()
    print()

    ensembles.print_output(input_ans)
    entropy.print_output(input_ans)


print_task1(input_ans_1)
