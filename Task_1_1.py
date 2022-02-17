# 1. Реализовать вывод информации о промежутке времени
# в зависимости от его продолжительности duration в секундах

duration = int(input('введите количество секунд: '))

if duration < 60:
    seconds = duration % 60
    print(seconds, 'сек.')
elif duration < 3600:
    minutes = duration // 60
    seconds = duration % 60
    print(minutes, 'мин.', seconds, 'сек.')
elif duration < 86400:
    hours = duration // 3600
    minutes = duration // 60 % 60
    seconds = duration % 60
    print(hours, 'ч.', minutes, 'мин.', seconds, 'сек.')
else:
    days = duration // 3600 // 24
    hours = duration // 3600 % 24
    minutes = duration // 60 % 60
    seconds = duration % 60
    print(days, 'дн.', hours, 'ч.', minutes, 'мин.', seconds, 'сек.')
