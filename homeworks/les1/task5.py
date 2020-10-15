"""
5. Запросите у пользователя значения выручки и издержек фирмы.
Определите, с каким финансовым результатом работает фирма
(прибыль — выручка больше издержек, или убыток — издержки больше выручки).
Выведите соответствующее сообщение. Если фирма отработала с прибылью,
вычислите рентабельность выручки (соотношение прибыли к выручке).
Далее запросите численность сотрудников фирмы и определите прибыль фирмы в расчете на одного сотрудника.
"""

a = int(input('input profit $ >>'))
b = int(input('input costs $ >>'))


if a > b:
    print(f"the company is profitable. profit {a / b*100-100:.0f}%")
    staff = int(input('how staff >>'))
    print(f"Congratulations, profit 1 staff -  {(a - b)/staff:}$")
elif a == b:
    print("the company operates without profit and without loss")
else:
    print("leaving. the company is unprofitable.")

