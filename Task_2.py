# Создать список, состоящий из кубов нечётных чисел от 1 до 1000 (куб X - третья степень числа X)

list_of_numbs = []
for num_01 in range(1, 1000, 2):
    list_of_numbs.append(num_01 ** 3)

# Вычислить сумму тех чисел из этого списка, сумма цифр которых делится нацело на 7

result_01 = 0
for num_02 in list_of_numbs:
    digit_sum = 0
    for digit_num in str(num_02):
        digit_sum += int(digit_num)
    if digit_sum % 7 == 0:
        result_01 += num_02
print(result_01)


# К каждому элементу списка добавить 17 и заново вычислить сумму
# тех чисел из этого списка, сумма цифр которых делится нацело на 7.

result_02 = 0
for num_03 in list_of_numbs:
    num_03 += 17
    digit_sum = 0
    for digit_num in str(num_03):
        digit_sum += int(digit_num)
    if digit_sum % 7 == 0:
        result_02 += num_03
print(result_02)
