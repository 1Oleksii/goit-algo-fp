import random
import matplotlib.pyplot as plt

# Функція для симуляції кидків двох кубиків
def monte_carlo_dice_simulation(num_trials):
    # Словник для підрахунку частоти появи сум
    sum_counts = {total: 0 for total in range(2, 13)}
    
    # Імітація кидків кубиків
    for _ in range(num_trials):
        die1 = random.randint(1, 6)  # Кидок першого кубика
        die2 = random.randint(1, 6)  # Кидок другого кубика
        total = die1 + die2          # Сума результатів
        
        sum_counts[total] += 1       # Підрахунок появи суми
    
    # Обчислення ймовірностей
    probabilities = {total: count / num_trials for total, count in sum_counts.items()}
    return probabilities

# Кількість симуляцій
num_trials = 1_000_000

# Запуск симуляції
probabilities = monte_carlo_dice_simulation(num_trials)

# Вивід результатів у вигляді таблиці
print("Sum | Probability (Monte Carlo) | Probability (Analytical)")
print("----|--------------------------|-------------------------")

# Аналітичні ймовірності згідно з теорією
analytical_probs = {
    2: 1/36, 3: 2/36, 4: 3/36, 5: 4/36, 6: 5/36, 7: 6/36,
    8: 5/36, 9: 4/36, 10: 3/36, 11: 2/36, 12: 1/36
}

for total in range(2, 13):
    monte_prob = probabilities[total] * 100
    analytical_prob = analytical_probs[total] * 100
    print(f"{total:>3} | {monte_prob:>22.2f}% | {analytical_prob:>21.2f}%")

# Побудова графіка ймовірностей
plt.bar(probabilities.keys(), [p * 100 for p in probabilities.values()], alpha=0.7, label='Monte Carlo')
plt.plot(list(analytical_probs.keys()), [p * 100 for p in analytical_probs.values()],
         color='red', marker='o', linestyle='dashed', linewidth=2, markersize=6, label='Analytical')

plt.title('Probability Distribution of Sums of Two Dice')
plt.xlabel('Sum of Dice')
plt.ylabel('Probability (%)')
plt.xticks(range(2, 13))
plt.legend()
plt.grid(True)
plt.show()
