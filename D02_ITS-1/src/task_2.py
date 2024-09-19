import math

weight = float(input("Введите вес пациента: "))
days = int(input("Введите количество дней в курсе лечения: "))
dose_per_day_mg = 10 * weight
tablets_per_day = dose_per_day_mg / 250
tablets_per_dose = round(tablets_per_day / 2, 1)
total_tablets = tablets_per_day * days
tablets_per_pack = 50
packs_needed = math.ceil(total_tablets / tablets_per_pack)

print(f"\nНужно принимать по {tablets_per_dose} таблетки(-e) 2 раза в день")
print(f"Необходимо {packs_needed} упаковка(-ки/-ок) по 50 таблеток (250мг) на весь курс лечения")
