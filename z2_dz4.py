# Задайте последовательность чисел. Напишите программу, которая выведет список 
# неповторяющихся элементов исходной последовательности.
import random

mas_1 = []
for i in range(10):
    mas_1.append(random.randint(1, 10))
print(mas_1)
mas_2 = []
for i in mas_1:
   if mas_1.count(i) == 1:
       mas_2.append(i)
print(mas_2)