"""
1.. Поработайте с переменными, создайте несколько,
выведите на экран, запросите у пользователя несколько чисел и строк
и сохраните в переменные, выведите на экран.
"""

this_year = 2020
name = input('input your name \n:>>')
surname = input('input your surname \n:>>')
age = int(input('input your age \n:>>'))
city = input('input your Place of Birth \n:>>')

full_user_data = f'Hi {name} {surname} {this_year - age} born in. From {city} City'
print(full_user_data)
