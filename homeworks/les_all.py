
"""
PEP-8
Свод правил


# todo Объяснить типы
# Обычный строчный комментарий
some_variabale: int = 1 # int это целые числа

# какой ты тип данных ?
# print(type(some_variabale))

mass: float = 22
# float число с дробным значением int это целые числа str - строка
street_name = 'Lenyna 40 122131331'

mass2 = 344.55

mass3 = mass + mass2
mass4 = some_variabale + mass2
print(mass4)

home_number = 33
b = '12'
print(b + str(home_number)) # в данном случае получается что номер дома становится строка и они просто прописываются текстом

print(int(b) + home_number) # инт присвает тексту целое число и поэтому сумма получается

a = 'hello '
print(a * 3)


'''
1.. Поработайте с переменными, создайте несколько,
выведите на экран, запросите у пользователя несколько чисел и
строк и сохраните в переменные, выведите на экран.
'''
this_year = 2020
name = input('input your name \n:>>') # /n это перенос строки
surname = input('input yr surname \n:>>' )
age = int(input('input yr age \n:>>'))
city = input( 'input yr Place of Birth \n:>>' )
# b_year = this_year-int(age)
full_user_data = f'Hi {name} {surname} {this_year - age} born in. From {city} City'

# print(name, surname, sep='--', end="|") # sep это перенос строки, энд это пробел
# print('you were born in - ', b_year, 'yr. in', city, ' City')
print(full_user_data)

b_one = True
b_two = False

if age >=18:
    print("Acsess full") #иф это не вопрос, это утверждение
    if age >30:
        print('now All at home')
elif age >=16: # иначе если
    print('Acsess content 16+')
elif age <12:
    print('conent watch mult 12+')
else: # абсолюдно иначе
    print('Acsess ')


if -
elif
else
in (проверяет естьли заданное значение, например -(a = 'hello'
'l' in a
True
's' in a
False))
>
<
>=
<=
not
and
or

-------------------------

les2

var_int = 1
var_str = 'строка'
var_bool = True
var_float = 12.234

Классы типы данных
Изменяемые
Не изменяемы типы данных


# коллекции итерируемые



var_list = [1,2, 'hello', 'world' True, ] #Список изменяемый
users = []

while True:
    user_template = {}
    user_template ['name'] = input()



for item in users:
    print(item)
    if item['name'] == 'asdgfs':
        break

for item in users:
    if not item['name'].islower():
        item['name'] = item ['item'].title()
    print(item)
print(users)


# for el in reversed("abrakadbra"):
#    print(el)

line = list('5someline6')
print(line)
print(type(line))

lineT = (4, 234, 45.8, "text", "word", "el", True, None, -77, False)


# print(lineT)
# print(type(lineT))

def my_type(el):
    for el in range(len(lineT)):
        print(type(lineT[el]))
    return


my_type(lineT)

"""

# les3 20.10.2020 __________________________________________________________________________


