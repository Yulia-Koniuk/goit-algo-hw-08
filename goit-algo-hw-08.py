import heapq

def min_cost_to_merge_cables(cables):
    heapq.heapify(cables)  # перетворюємо список кабелів у піраміду

    total_cost = 0
    merge_steps = []  # зберігаємо кроки об'єднання

    while len(cables) > 1:
        # Витягуємо два найдовші кабелі з піраміди
        cable1 = heapq.heappop(cables)
        cable2 = heapq.heappop(cables)

        # Об'єднуємо два кабелі
        merged_cable = cable1 + cable2

        # Додаємо витрати на об'єднання до загальних витрат
        total_cost += merged_cable

        # Додаємо крок об'єднання до списку
        merge_steps.append((cable1, cable2))

        # Додаємо об'єднаний кабель назад до піраміди
        heapq.heappush(cables, merged_cable)

    return total_cost, merge_steps

# Приклад використання
cables = [12, 11, 13, 5, 6, 7]
min_cost, merge_steps = min_cost_to_merge_cables(cables)
print("Мінімальні загальні витрати на об'єднання всіх кабелів:", min_cost)
print("Порядок об'єднання кабелів, який мінімізує загальні витрати:")
for step in merge_steps:
    print(step[0], "+", step[1])


'''
Мінімальні загальні витрати на об'єднання всіх кабелів: 137

Порядок об'єднання кабелів, який мінімізує загальні витрати:
5 + 6
7 + 11
11 + 12
13 + 18
23 + 31
'''