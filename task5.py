import uuid
import networkx as nx
import matplotlib.pyplot as plt
from collections import deque

# Клас Node описує вузол дерева
class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key
        self.color = "#AAAAAA"
        self.id = str(uuid.uuid4())

# Додає вузли та ребра до графа
def add_edges(graph, node, pos, x=0, y=0, layer=1):
    if node is not None:
        graph.add_node(node.id, color=node.color, label=node.val)
        if node.left:
            graph.add_edge(node.id, node.left.id)
            l = x - 1 / 2 ** layer
            pos[node.left.id] = (l, y - 1)
            add_edges(graph, node.left, pos, x=l, y=y - 1, layer=layer + 1)
        if node.right:
            graph.add_edge(node.id, node.right.id)
            r = x + 1 / 2 ** layer
            pos[node.right.id] = (r, y - 1)
            add_edges(graph, node.right, pos, x=r, y=y - 1, layer=layer + 1)
    return graph

# Візуалізує граф
def draw_tree(tree_root):
    tree = nx.DiGraph()
    pos = {tree_root.id: (0, 0)}
    tree = add_edges(tree, tree_root, pos)
    colors = [tree.nodes[node]['color'] for node in tree.nodes()]
    labels = {node: tree.nodes[node]['label'] for node in tree.nodes()}
    plt.figure(figsize=(8, 5))
    nx.draw(tree, pos=pos, labels=labels, arrows=False, node_size=2500, node_color=colors)
    plt.show()

# Побудова дерева з масиву без рекурсії
def build_heap_tree(arr):
    if not arr:
        return None
    nodes = [Node(val) for val in arr]
    for i in range(len(arr)):
        if 2 * i + 1 < len(arr):
            nodes[i].left = nodes[2 * i + 1]
        if 2 * i + 2 < len(arr):
            nodes[i].right = nodes[2 * i + 2]
    return nodes[0]

# Генерація градієнта кольорів від темно-синього до світло-блакитного
def generate_color_gradient(n):
    colors = []
    for i in range(n):
        # Градієнт між #0000FF (темно-синій) і #ADD8E6 (світло-блакитний)
        r = int((173 * i) / (n - 1))
        g = int((216 * i) / (n - 1))
        b = int(255 - (255 - 230) * i / (n - 1))  # від 255 до 230
        hex_color = f"#{r:02X}{g:02X}{int(b):02X}"
        colors.append(hex_color)
    return colors

# Ітеративний підрахунок вузлів
def count_nodes(root):
    if not root:
        return 0
    count = 0
    queue = deque([root])
    while queue:
        node = queue.popleft()
        count += 1
        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)
    return count

# Ітеративне скидання кольору
def reset_colors(root):
    if not root:
        return
    queue = deque([root])
    while queue:
        node = queue.popleft()
        node.color = "#AAAAAA"
        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)

# Обхід в ширину
def bfs_visualization(root):
    if not root:
        print("Дерево порожнє")
        return
    queue = deque([root])
    result = []
    colors = generate_color_gradient(count_nodes(root))
    i = 0
    while queue:
        node = queue.popleft()
        node.color = colors[i]
        i += 1
        result.append(node.val)
        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)
    print("BFS order:", result)
    draw_tree(root)

# Обхід в глибину
def dfs_visualization(root):
    if not root:
        print("Дерево порожнє")
        return
    stack = [root]
    result = []
    colors = generate_color_gradient(count_nodes(root))
    i = 0
    while stack:
        node = stack.pop()
        node.color = colors[i]
        i += 1
        result.append(node.val)
        if node.right:
            stack.append(node.right)
        if node.left:
            stack.append(node.left)
    print("DFS order:", result)
    draw_tree(root)

# Початковий масив для дерева
heap_array = [1, 3, 5, 7, 9, 8]

# Побудова дерева
heap_root = build_heap_tree(heap_array)

# Виведення обходу в ширину
print("BFS Traversal")
bfs_visualization(heap_root)

# Скидання кольорів
reset_colors(heap_root)

# Виведення обходу в глибину
print("DFS Traversal")
dfs_visualization(heap_root)
