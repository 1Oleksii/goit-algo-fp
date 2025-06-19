import uuid
import networkx as nx
import matplotlib.pyplot as plt

# Клас Node описує вузол дерева
class Node:
    def __init__(self, key, color="skyblue"):
        self.left = None  # Лівий нащадок
        self.right = None  # Правий нащадок
        self.val = key  # Значення вузла
        self.color = color  # Колір вузла для візуалізації
        self.id = str(uuid.uuid4())  # Унікальний ідентифікатор для візуалізації в графі

# Функція для додавання вузлів та ребер у граф для візуалізації
def add_edges(graph, node, pos, x=0, y=0, layer=1):
    if node is not None:
        # Додаємо вузол до графа
        graph.add_node(node.id, color=node.color, label=node.val)
        
        # Додаємо лівого нащадка, якщо існує
        if node.left:
            graph.add_edge(node.id, node.left.id)
            l = x - 1 / 2 ** layer  # Зміщення по осі X
            pos[node.left.id] = (l, y - 1)  # Координати для лівого вузла
            add_edges(graph, node.left, pos, x=l, y=y - 1, layer=layer + 1)
        
        # Додаємо правого нащадка, якщо існує
        if node.right:
            graph.add_edge(node.id, node.right.id)
            r = x + 1 / 2 ** layer
            pos[node.right.id] = (r, y - 1)
            add_edges(graph, node.right, pos, x=r, y=y - 1, layer=layer + 1)

    return graph

# Функція для візуалізації дерева з кореневого вузла
def draw_tree(tree_root):
    tree = nx.DiGraph()  # Створюємо орієнтований граф
    pos = {tree_root.id: (0, 0)}  # Початкова позиція кореня

    tree = add_edges(tree, tree_root, pos)

    # Отримуємо кольори та мітки для візуалізації
    colors = [node[1]['color'] for node in tree.nodes(data=True)]
    labels = {node[0]: node[1]['label'] for node in tree.nodes(data=True)}

    # Малюємо граф
    plt.figure(figsize=(8, 5))
    nx.draw(tree, pos=pos, labels=labels, arrows=False, node_size=2500, node_color=colors)
    plt.show()

# Функція будує дерево на основі масиву купи (за рівневим порядком)
def build_heap_tree(arr, index=0):
    if index >= len(arr):
        return None
    node = Node(arr[index])  # Створюємо вузол з елементу масиву
    node.left = build_heap_tree(arr, 2 * index + 1)  # Лівий нащадок
    node.right = build_heap_tree(arr, 2 * index + 2)  # Правий нащадок
    return node

# Масив, що представляє бінарну мін-купу
heap_array = [1, 3, 5, 7, 9, 8]

# Побудова дерева з купи
heap_root = build_heap_tree(heap_array)

# Візуалізація дерева купи
draw_tree(heap_root)
