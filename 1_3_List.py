# Списки treinee (A1 повтор)
# Создать список чисел от 1 до 10
list_one = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
list_one = list(range(1, 11))
print(list_one)
# Добавить элемент в конец списка
list_one.append(11)
print(list_one)
# Удалить элемент по индексу
list_one.pop(-1)
print(list_one)
# Найти индекс конкретного элемента
print(list_one.index(10))
# # Развернуть список в обратном порядке
list_one.sort(reverse=True)
print(list_one)
# Отсортировать список на возрастание
list_one.sort()
print(list_one)
# Создать список списков (матрицу)
