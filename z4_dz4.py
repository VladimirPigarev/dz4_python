# Задана натуральная степень k. Сформировать случайным образом список коэффициентов 
# (значения от 0 до 100) многочлена и записать в файл многочлен степени k.
# Пример:
# - k=2 => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0

import random
from random import randint
from os import path
import os.path

k = int(input('Введите натуральную степень К : '))
if k == 0:
    s1 = 'x^0=1'
else:
    list_x = []
    vk = k
    for i in range(k+1):
        if i <=k:
            x = random.randint(0,k)
            list_x.append(str(x)+'*x^'+str(vk)+'+')
            vk = vk-1
        else:
            x = random.randint(0, k)
            list_x.append(str(x))
            break
s2 = '3*x^k+5*x^(k-1)+2*x^(k-2)+свободный член'
for i in range(k+1):
    if i <= (k+1):
        s2 = s2 + list_x[i]
        s2 = s2+'=0'
# s1.replace('^', '**')
s2.replace('^', '**')
f = open('z4.txt', 'a')
if k ==0:
    f.write(s1)
    f.close
if k != 0:
    f.write(s2)
    f.close
f = open('z4.txt', 'r')
while True:
    rez = f.readline()
    if not rez:
        break
    f.close
print(rez.strip())

