# Оголошення вузла однозв'язного списку
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

# Клас для роботи з однозв'язним списком
class LinkedList:
    def __init__(self):
        self.head = None

    # Додавання нового елемента в кінець списку
    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node

    # Виведення всіх елементів списку
    def print_list(self):
        current = self.head
        while current:
            print(current.data, end=' -> ')
            current = current.next
        print('None')

    # Реверсування списку (зміна напрямку посилань)
    def reverse(self):
        # Ініціалізуємо попередній вузол як None
        prev = None
        current = self.head
        while current:
            next_node = current.next  # зберігаємо наступний вузол
            current.next = prev       # змінюємо напрямок зв'язку
            prev = current            # переміщаємо попередній вперед
            current = next_node       # переходимо до наступного вузла
        self.head = prev

    # Сортування злиттям для списку
    def merge_sort(self, head):
        if not head or not head.next:
            return head

        middle = self.get_middle(head)
        next_to_middle = middle.next
        middle.next = None

        left = self.merge_sort(head)
        right = self.merge_sort(next_to_middle)

        return self.sorted_merge(left, right)

    # Отримати середину списку (використовується в merge sort)
    def get_middle(self, head):
        if not head:
            return head
        slow = head
        fast = head
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
        return slow

    # Об'єднання двох відсортованих списків в один відсортований
    def sorted_merge(self, a, b):
        if not a:
            return b
        if not b:
            return a

        if a.data <= b.data:
            result = a
            result.next = self.sorted_merge(a.next, b)
        else:
            result = b
            result.next = self.sorted_merge(a, b.next)
        return result

    # Запуск сортування списку
    def sort(self):
        self.head = self.merge_sort(self.head)

# Приклад використання
if __name__ == "__main__":
    # Створення першого списку
    list1 = LinkedList()
    list1.append(5)
    list1.append(3)
    list1.append(8)
    list1.append(1)

    print("Оригінальний список:")
    list1.print_list()

    # Реверсування
    list1.reverse()
    print("Реверсований список:")
    list1.print_list()

    # Сортування
    list1.sort()
    print("Відсортований список:")
    list1.print_list()

    # Створення другого відсортованого списку
    list2 = LinkedList()
    list2.append(2)
    list2.append(4)
    list2.append(7)
    list2.append(9)
    list2.sort()

    print("Другий відсортований список:")
    list2.print_list()

    # Об'єднання
    merged = LinkedList()
    merged.head = list1.sorted_merge(list1.head, list2.head)
    print("Об'єднаний відсортований список:")
    merged.print_list()
