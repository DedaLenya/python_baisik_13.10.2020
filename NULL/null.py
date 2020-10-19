"""
# определяем тип переменной
person_name = 'Max'
age = 30
period = 3.2
is_good = True
person = None
print(type(person_name))
print(type(age))
print(type(period))
print(type(is_good))
print(type(person))


# str - это строка
# int - целое число
# float - число с плавающей точкой
# bool - булевые числа, ЛОГИЧЕСКИЙ тип данных, правда или ложь
# NoneType -
Конкатинация - это склеивание данных


# sep - сепаратор, фукция котора в принте разделяет фукции любым знаком. пример
print('stroka', 40, 40.5, True, None, sep='***')
# end='\n' это перенос строки или убирает её, приклеивает наверх
print('stroka', 40, 40.5, True, None, end='--------------')
print('stroka', 40, 40.5, True, None)


# что бы не спросили в инпут, это всегда будет строка, что бы сделать числом вначале вставляем ИНТ
result = int(input('>>'))
print(result)
print(type(result))


ale = 71
age = int(input('how old are U?:'))
print('Your universary yes', age % 5 == 0)

# not and or, != не равно или еще можно перед фукцией поставить not

print('У вас НЕ юбилей', age % 5 != 0)
print('У вас НЕ юбилей', not age % 5 == 0)

# and
print('У васю юбил И возраст меньше средней жизни', age %  5 == 0 and age <ale)

# or
print('У вас юбил ИЛИ возраст меньше средней жизни', age % 5 == 0 or age <ale)

# приоритет в логических выражениях
print((3>2 and (6 <5 or 3 < 2)) and 0 == 0)


age = int(input('input your age:'))
# если возраст меньше 18 лет
# Вывести на экран "доступ запрещен"
# else это условие если не выполняется if
# elif это дополнительный код (альтернативное условие) к if и элиф может быть сколько угодно много
# if может быть внутри блоков , в любой блок. вложенность
if age < 18:
    print("эдоступ запрещен")
elif age == 18:
    print("вам только 18")
    print("что с вами делать")
elif age > 18 and age <25:
    print("вы отдельная категория пользователей")
else:
    print('acsess aproved')
    # проверим на юбилей
    if age % 5 == 0:
        print('поздравляем у вас в этом году юбилей')

number = 43
value = int(input('введите число от 1 до 100>>'))
if value == number:
    print('Угадали!!')
else:
    if value > number:
        print("Не верно, введенное число слишком большое")
    else:
        print("Не верно, введенное число слишко маленькое")



# ЦИКЛЫ while *********************************************************
# это цикл с условиями, while условие : действие1 дейстиве2 и т д
name = input(' кто создатель python ?>')
while name != 'Гвидо':
    print(' Не верно, пробуйте еще')
    name = input(' кто создатель python ?>')
print(' верно ')


# вывод чисел от 0 до 100
# вывод числе от 0 до n , где эн вводит пользователь
# вывод четных чисел от 0 до эн

number = 0
n = int(input(' число введите>>'))
while number <= n:
    if number % 2 == 0: # делится на 2, значит четное
        print(number) # поэтому печатаем
    # number = number + 1
    number += 1 # это будет тоже самое что строка сверху



# break позволяет выйти из цикла в независимотси выполнилось условие или нет
name = None

while True:
    name = input(' кто создатель python ?>')
    if name == 'Гвидо':
        break
    print(' не верно ')
print(' верно ')

# continue переход на след. итерацию цикла (команды в цикле после continue не выплняются)


number = 0
n = int(input(' число введите>>'))

while number <= n:
    if number % 2 == 0: # делится на 2, значит четное
        number += 1 # это будет тоже самое что строка сверху
        continue
    print(number)  # поэтому печатаем
    number += 1


# while-else в блоке else (после while ) мы выполеняем действиея после того
#как вышли из цикла while когда условие цикла стало не верным (False)

number = 0

while number <=100:
    print(number)
    number += 1
    #if number == 33:
     #   break
else:
    print('else - end')
print('end')


ДОМАШНЕЕ ЗАДАНИЕ 1-3 ПУНКТЫ

while True:
    number = int(input('введите число 0-10>>'))
    if number > 0 and number < 10:
        break
    print(' НЕ верно, число должно быть от 0 до 10')
    continue
number1 = number ** 2
print('ваше число во второй степени - ', number1)




name = input(' имя -')
surname = input(' фамилия-')
age = int(input(' ваш возрас -'))
weight = int(input(' ваш вес-'))

if age <=30 and weight >= 50 and weight <=120:
    print(name, surname, 'хорошее состояние')
elif age > 30 and age <= 40 and (weight > 50 or weight > 120):
    print(name, surname, ' займись собой')
elif age >= 40 and (weight < 50 or weight > 120):
    print(name, surname, ' иди к врачу')


# СТОКИ str
# можно вычислить символ по индексу, индекс указывается в []
# все индексы начинаются с 0. отрицательные индексы допускаются

friend = 'Максим'
n = int(input(' введите номер буквы>> '))
letter = friend[n]
print(n+1, 'я буква имени - ', letter)
print(friend[-1])


# Срезы 1 - с какого символа, 4 - по какой символ, 4: срез с начала строки

friend = 'Максим'
print(friend[1:4])



# len методы и строки, может определить длину строки
# len(friend) - длинна строки (сколько в ней символов)
# friend.find('a') - ищем символ а в строке
# friend.split() - разбиение строки через пробел
# friend.isdigit() - строка состоит из чисел

friends = 'Максим Леонид'
print(friends)

print(len(friends))
print(friends.find('нид'))
friends = 'Максим-Леонид'
print(friends.split('-')) # можно не только пробелы разделить, а любой другой знак

print(friends.isdigit()) # строка не из цифр, поэтому выдает false. работает похоже только на то что в скобках

number = '123'
print(number.isdigit())

print(friends.upper()) # все буквы делает большими заглавными
print(friends.lower()) # все буквы делает меленькими строчными


# Методы строк строчек
# help(str) или выпадающая подсказка в pycharm или сайт питонворлд

# ФОРМАТИРОВАНИЕ СТРОК
# конкантенация (не рекомендуется) - это склеиванеи строк
# %
# format (рекомендуется)
name = 'Leo'
age = 30
# конкатенация не плохо читается код и нужны пробелы
hellou_str = ' привет, ' + name + ' тебе ' + str(age) + ' лет '
print(hellou_str)
# % строка %s и число %d
hellou_str = ' Привет %s тебе %d лет' % (name, age)
print(hellou_str)

# 3 format
hellou_str = ' Привет {} тебе {} лет ' .format(name, age)
print(hellou_str)

top5 = ' Первые 5 мест на соревнованиях: 1. Иванов. 2. Петров. ' \
       '3. Сидоров. 4. Орлов. 5.Соколов.'
start = top5.find('1')
end = top5.find('4')
top3 = top5[start: end]
result = ' Поздравляем {} с успехом!'.format(top3.upper())
print(result)
"""
# Списки, определение, методы, оператор in, Кортежи
# list списки

# можно объявить пустой список
empty_list = []

# можно объявить список и сразу заполнить его элементами
friends = ['Max' , 'Leo', 'Kate']

# тип списка - list
print(type(friends))


