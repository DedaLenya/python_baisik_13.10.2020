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
"""

'''
1. Поработайте с переменными, создайте несколько, 
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

"""
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
"""
