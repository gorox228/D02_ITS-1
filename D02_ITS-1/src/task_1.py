import math
days = int(input("Введите количество дней в курсе лечения: "))

tablets_per_day = 1  

total_tablets = tablets_per_day * days

tablets_per_pack = 50

packs_needed = math.ceil(total_tablets / tablets_per_pack)

print(f"Необходимо {packs_needed} упаковка(-ки/-ок) по 50 таблеток (250мг) на весь курс лечения")
