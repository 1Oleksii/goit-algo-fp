# Функція жадібного алгоритму
# Вибирає страви за співвідношенням калорій до вартості, не перевищуючи бюджет
def greedy_algorithm(items, budget):
    # Сортуємо страви за спаданням калорійності на одиницю вартості
    sorted_items = sorted(items.items(), key=lambda x: x[1]['calories'] / x[1]['cost'], reverse=True)
    
    chosen = []
    total_cost = 0
    
    for name, info in sorted_items:
        if total_cost + info['cost'] <= budget:
            chosen.append(name)
            total_cost += info['cost']
    
    return chosen

# Функція динамічного програмування
# Знаходить оптимальний набір страв для максимізації калорійності при заданому бюджеті
def dynamic_programming(items, budget):
    names = list(items.keys())
    costs = [items[name]['cost'] for name in names]
    calories = [items[name]['calories'] for name in names]
    
    n = len(items)
    # Таблиця dp[i][w] - максимальна калорійність, яку можна отримати, розглядаючи перші i предметів і бюджет w
    dp = [[0] * (budget + 1) for _ in range(n + 1)]
    
    for i in range(1, n + 1):
        for w in range(budget + 1):
            if costs[i - 1] <= w:
                dp[i][w] = max(dp[i - 1][w], dp[i - 1][w - costs[i - 1]] + calories[i - 1])
            else:
                dp[i][w] = dp[i - 1][w]
    
    # Відновлення вибраних страв
    w = budget
    chosen = []
    for i in range(n, 0, -1):
        if dp[i][w] != dp[i - 1][w]:
            chosen.append(names[i - 1])
            w -= costs[i - 1]
    
    chosen.reverse()
    return chosen


# Приклад використання:
items = {
    "pizza": {"cost": 50, "calories": 300},
    "hamburger": {"cost": 40, "calories": 250},
    "hot-dog": {"cost": 30, "calories": 200},
    "pepsi": {"cost": 10, "calories": 100},
    "cola": {"cost": 15, "calories": 220},
    "potato": {"cost": 25, "calories": 350}
}

budget = 100

print("Greedy algorithm selection:", greedy_algorithm(items, budget))
print("Dynamic programming selection:", dynamic_programming(items, budget))
