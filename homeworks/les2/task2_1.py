""" a) Создать список и заполнить его элементами различных типов данных.
    c) Элементы списка можно не запрашивать у пользователя, а указать явно, в программе.
    b) Реализовать скрипт проверки типа данных каждого элемента. Использовать функцию type()
    для проверки типа.
"""
lineT = (4, 234, 45.8, "text", "word", "el", True, None, -77, False)
def my_type(el):
    for el in range(len(lineT)):
        print(type(lineT[el]))
    return
    my_type(lineT)
