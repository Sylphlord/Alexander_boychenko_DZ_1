# Реализовать склонение слова «процент» во фразе «N процентов».
# Вывести эту фразу на экран отдельной строкой для каждого из чисел в интервале от 1 до 100

for persent in range(100):
    persent += 1
    if persent % 10 == 1:
        print(persent, 'процент')
    elif 1 < persent % 10 < 5:
        print(persent, 'процента')
    else:
        print(persent, 'процентов')
