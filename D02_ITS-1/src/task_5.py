import re
import math

def find_alt_ast(text):
    text_lower = text.lower()
    alt_match = re.search(r'алт\s*-\s*(\d+\.\d+)', text_lower)
    ast_match = re.search(r'аст\s*-\s*(\d+\.\d+)', text_lower)

    if alt_match and ast_match:
        alt_value = alt_match.group(1)
        ast_value = ast_match.group(1)
        return float(alt_value), float(ast_value)
    else:
        print("Не удалось найти АЛТ или АСТ в анализе.")
        exit()

analysis = input("Вставьте результаты анализов: ")
alt, ast = find_alt_ast(analysis)
separator = '-' * 50
print(separator)
print(f"АЛТ - {alt:.2f}")
print(f"АСТ - {ast:.2f}")
print(separator)
dose_per_kg = float(input("Введите среднюю суточную дозу в мг/кг (10 или 15): "))

if dose_per_kg not in [10, 15]:
    print(separator)
    print("Суточная доза не равна 10 или 15 мг/кг! Остальные дозы пока не рассчитываются!")
    print(separator)
    exit()
weight = float(input("Введите вес пациента: "))
days = int(input("Введите количество дней в курсе лечения: "))
dose_per_day_mg = dose_per_kg * weight
tablets_per_day = dose_per_day_mg / 250
total_tablets = tablets_per_day * days
tablets_per_pack = 50
packs_needed = math.ceil(total_tablets / tablets_per_pack)

print(separator)

if tablets_per_day % 1 == 0:
    tablets_per_dose = int(tablets_per_day / 2)
    print(f"Нужно принимать по {tablets_per_dose} таблетки(-e) 2 раза в день")
else:
    tablets_morning = math.floor(tablets_per_day / 2)
    tablets_evening = math.ceil(tablets_per_day / 2)
    print(f"Нужно принимать {tablets_morning} таблетку(-и) утром и {tablets_evening} таблетку(-и) вечером")

print(f"Необходимо {packs_needed} упаковка(-ки/-ок) по 50 таблеток (250мг) на весь курс лечения")
print(separator)
