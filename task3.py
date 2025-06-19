import heapq

# Функція реалізує алгоритм Дейкстри для зваженого графа
# Вона також зберігає попередників для побудови повного шляху
def dijkstra(graph, start):
    # Перевіряємо, чи граф не порожній
    if not graph:
        raise ValueError("Граф порожній")

    # Перевіряємо, чи існує стартова вершина у графі
    if start not in graph:
        raise ValueError("Стартова вершина відсутня в графі")

    # Ініціалізуємо відстані як нескінченність для всіх вершин
    distances = {vertex: float('inf') for vertex in graph}
    distances[start] = 0  # Відстань до стартової вершини = 0

    # Словник для збереження попередніх вершин (для відновлення шляху)
    previous = {vertex: None for vertex in graph}

    # Створюємо мін-купу (пріоритетну чергу), додаємо туди стартову вершину
    priority_queue = [(0, start)]  # (відстань, вершина)

    while priority_queue:
        # Вибираємо вершину з найменшою відстанню
        current_distance, current_vertex = heapq.heappop(priority_queue)

        # Якщо ми вже знайшли кращий шлях до цієї вершини — пропускаємо
        if current_distance > distances[current_vertex]:
            continue

        # Перевіряємо всіх сусідів поточної вершини
        for neighbor, weight in graph[current_vertex].items():
            distance = current_distance + weight

            # Якщо знайшли коротший шлях до сусіда — оновлюємо
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                previous[neighbor] = current_vertex
                heapq.heappush(priority_queue, (distance, neighbor))

    return distances, previous

# Функція для відновлення найкоротшого шляху до певної вершини
def reconstruct_path(previous, start, end):
    path = []
    current = end
    while current is not None:
        path.insert(0, current)
        current = previous[current]
    if path and path[0] == start:
        return path
    return []

# Приклад графа у вигляді словника суміжності
graph = {
    'A': {'B': 4, 'C': 2},
    'B': {'A': 4, 'C': 1, 'D': 5},
    'C': {'A': 2, 'B': 1, 'D': 8, 'E': 10},
    'D': {'B': 5, 'C': 8, 'E': 2, 'Z': 6},
    'E': {'C': 10, 'D': 2, 'Z': 3},
    'Z': {'D': 6, 'E': 3}
}

# Вибираємо стартову вершину
start_vertex = 'A'

# Запускаємо алгоритм Дейкстри
distances, previous = dijkstra(graph, start_vertex)

# Виводимо найкоротші відстані та шляхи до всіх вершин
print(f"Найкоротші відстані та шляхи від вершини {start_vertex}:")
for vertex in graph:
    distance = distances[vertex]
    path = reconstruct_path(previous, start_vertex, vertex)
    print(f"До вершини {vertex}: відстань = {distance}, шлях = {' -> '.join(path)}")
