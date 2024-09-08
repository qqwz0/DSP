def discrete_convolution(x, y):
    len_x = len(x)
    len_y = len(y)
    result_len = len_x + len_y - 1
    result = [0] * result_len

    for m in range(result_len):
        sum_value = 0
        for k in range(len_x):
            if 0 <= m - k < len_y:
                sum_value += x[k] * y[len_y - 1 - (m - k)]
        result[m] = sum_value

    return result

 
# Сигнали
x = [6, 5, 4]
y = [8, 1, 0]

x1 = [6, 4, 0, 1, 2, 3, 6, 4, 0, 3, 8, 7 ]
y1 = [4, 0, 8, 2, 7, 3]

x2 = [2, 6, 4, 0, 8, 2]
y2 = [6, 4, 0, 1, 2, 8, 6, 4, 0, 8, 3, 7 ]
# Виклик функції для обчислення згортки
discrete_convolution(x, y)

print(f"Результат згортки: {discrete_convolution(x, y)}")
print(f"Результат згортки: {discrete_convolution(x1, y1)}")
print(f"Результат згортки: {discrete_convolution(x2, y2)}")
