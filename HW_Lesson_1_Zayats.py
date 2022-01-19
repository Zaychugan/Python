# Задача-1: Поработайте с переменными, создайте несколько, выведите на экран,
# запросите у пользователя несколько чисел и строк и сохраните в переменные, выведите на экран.

a = input("Enter your name: ")
b = int(input("Enter your age: "))
c = float(input("Enter any number: "))

print(a, b, c)

# Задача-2: Пользователь вводит время в секундах.
# Переведите время в часы, минуты и секунды и выведите в формате чч:мм:сс.
# Используйте форматирование строк.

time_in_sec = int(input("Enter your local time in sec: "))
hours = time_in_sec // 3600
residue = time_in_sec % 3600
minutes = residue // 60
sec = residue % 60
print(f"Now is {hours}:{minutes}:{sec} ")

# Задача-3: Узнайте у пользователя число n. Найдите сумму чисел n + nn + nnn.
# Например, пользователь ввёл число 3. Считаем 3 + 33 + 333 = 369.

number = input("Enter number: ")
a = int(number + number)
b = int(number+number+number)
summa = int(number) + a + b

print(summa)

# Задача-4: Пользователь вводит целое положительное число.
# Найдите самую большую цифру в числе.
# Для решения используйте цикл while и арифметические операции.


number = input("Enter number: ")
x = 0
for i in number:
    while int(i) > x:
        x = int(i)
print(x)

# Задание-5:
# Запросите у пользователя значения выручки и издержек фирмы.
# Определите, с каким финансовым результатом работает фирма (прибыль — выручка больше издержек, или убыток — издержки больше выручки).
# Выведите соответствующее сообщение.
# Если фирма отработала с прибылью, вычислите рентабельность выручки (соотношение прибыли к выручке).
# Далее запросите численность сотрудников фирмы и определите прибыль фирмы в расчете на одного сотрудника.

proceed = int(input("Enter proceed: "))
outlay = int(input("Enter outlay: "))
if proceed > outlay:
    profitability = proceed-outlay
    rent = profitability/proceed
    print(f"Great work. You have {profitability} profitability")
    worker = int(input("How many people work: "))
    print(f"{profitability/worker} for one worker")
elif proceed == outlay:
    print("No bad")
else:
    print("Good luck")

# Задача-6: Спортсмен занимается ежедневными пробежками. В первый день его результат составил a километров.
# Каждый день спортсмен увеличивал результат на 10 % относительно предыдущего.
# Требуется определить номер дня, на который общий результат спортсмена составить не менее b километров.
# Программа должна принимать значения параметров a и b и  выводить одно натуральное число — номер дня.

a = float(input("Enter start: "))
b = float(input("Enter finish: "))
day = 1
if a > b:
    print(day)
while a < b:
    a = a + a/10
    day += 1
print(day)

