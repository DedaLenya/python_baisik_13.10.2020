"""
2.. Пользователь вводит время в секундах.
Переведите время в часы, минуты и секунды и выведите в формате
чч:мм:сс. Используйте форматирование строк.
"""

ss = int(input('input time in second >>'))
print('fine, you enter', ss, 'second or:')
hh = str(ss//3600)
mm = (ss//60) % 60
ss1 = ss % 60
if mm < 10:
    mm = '0'+str(mm)
else:
    mm = str(mm)
if ss1 < 10:
    ss1 = '0'+str(ss1)
else:
    ss1 = str(ss1)
print(hh+' hr:'+mm+' min:'+ss1+' sec')
