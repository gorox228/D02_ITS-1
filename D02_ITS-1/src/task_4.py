import math

dose_per_kg = float(input("Введите среднюю суточную дозировку в мг/кг (10 или 15): "))

if dose_per_kg not in [10, 15]:
    print("Суточная дозировка не равна 10 или 15 мг/кг! Остальные дозировки пока не рассчитываются!")
    exit()

weight = float(input("Введите вес пациента: "))
days = int(input("Введите количество дней в курсе лечения: "))
dose_per_day_mg = dose_per_kg * weight
tablets_per_day = dose_per_day_mg / 250
total_tablets = tablets_per_day * days
tablets_per_pack = 50
packs_needed = math.ceil(total_tablets / tablets_per_pack)

if tablets_per_day % 1 == 0:
    # Четное количество
    tablets_per_dose = int(tablets_per_day / 2)
    print(f"\nНужно принимать по {tablets_per_dose} таблетки(-e) 2 раза в день")
else:
    
    tablets_morning = math.floor(tablets_per_day / 2)
    tablets_evening = math.ceil(tablets_per_day / 2)
    print(f"\nНужно принимать {tablets_morning} таблетку(-и) утром и {tablets_evening} таблетку(-и) вечером")

print(f"Необходимо {packs_needed} упаковка(-ки/-ок) по 50 таблеток (250мг) на весь курс лечения")
