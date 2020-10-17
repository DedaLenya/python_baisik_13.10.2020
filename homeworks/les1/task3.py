"""
3.. Узнайте у пользователя число n.
Найдите сумму чисел n + nn + nnn.
Например, пользователь ввёл число 3.
Считаем 3 + 33 + 333 = 369.
"""

n = str(input('pls, input any number >>'))
a = int(n)
b = int(n+n)
c = int(n+n+n)
x = a+b+c
print(x)
