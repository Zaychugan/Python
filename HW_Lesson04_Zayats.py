def simple_calc():
    x = float(input('Введите количество отработанных часов : '))
    y = float(input('Введите суммы оплаты труда за 1 час : '))
    c = float(input('Укажите размер премии - '))
    pay = x * y
    return pay + c
print(f'Размер заработной платы составил: {simple_calc() }')

#2. Представлен список чисел.
# Необходимо вывести элементы исходного списка, значения которых больше предыдущего элемента.
import random
list1 = random.sample(range(1, 1000), 20) #генерирует числа от 1 до 1000, всего этих чисел 20
print(list1)
list2 = []
for el in range(len(list1) - 1):
    if list1[el] < list1[el+1]:
        list2.append(list1[el+1])
print(list2)

#3. Для чисел в пределах от 20 до 240 найти числа, кратные 20 или 21. Необходимо решить задание в одну строку.
print([el for el in range(20, 241) if el % 20 == 0 or el % 21 == 0])

#4. Представлен список чисел.
# Определить элементы списка, не имеющие повторений.
# Сформировать итоговый массив чисел, соответствующих требованию.
# Элементы вывести в порядке их следования в исходном списке.
# Для выполнения задания обязательно использовать генератор.
list1 = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]
list2 = [el for el in list1 if list1.count(el) == 1]
print(list2)

#5.Реализовать формирование списка, используя функцию range() и возможности генератора.
# В список должны войти четные числа от 100 до 1000 (включая границы).
# Необходимо получить результат вычисления произведения всех элементов списка.
list = [el for el in range(100, 1001) if el % 2 == 0]
print(list) # выводит список четных чисел от 100 до 1000
from functools import reduce
def my_func(el_p, el):
    return el_p * el
print(reduce(my_func, list)) #выводит произведение четных чисел от 100 до 1000

#6. Реализовать два небольших скрипта:
# а) итератор, генерирующий целые числа, начиная с указанного,
# Например, выводим целые числа, начиная с 3, а при достижении числа 10 завершаем цикл
def gen1():
    a = int(input('Введите стартовое число: '))
    from itertools import islice
    from itertools import count

    for i in islice(count(a), 10): #генерирует 10 чисел начиная с указанного
        print(i)
gen1()

# б) итератор, повторяющий элементы некоторого списка, определенного заранее.
# необходимо предусмотреть условие, при котором повторение элементов списка будет прекращено.
def gen2():
    list = [1, 107, None, "this_list"]

    from itertools import islice
    from itertools import cycle

    for el in islice(cycle(list), 10): #повторение элементов списка будет прекращено после 10ого повторения
        print(el)
gen2()

# 7.Реализовать генератор с помощью функции с ключевым словом yield, создающим очередное значение.
# При вызове функции должен создаваться объект-генератор.
# Функция должна вызываться следующим образом: for el in fact(n).
# Функция отвечает за получение факториала числа, а в цикле необходимо выводить только первые n чисел, начиная с 1! и до n!.
from itertools import count
from math import factorial
def factgen():
    for el in count(1):
        yield factorial(el)
gen = factgen()
n = 0
for elem in gen: #цикл выводит только первые 6 чисел
    if n < 6:
        print(elem)
        n += 1
    else:
        break
