# Напишите программу, которая принимает на вход координаты точки (X и Y), 
# причём X ≠ 0 и Y ≠ 0 и выдаёт номер четверти плоскости, 
# в которой находится эта точка (или на какой оси она находится).

# Пример:

# - x=34; y=-30 -> 4
# - x=2; y=4-> 1
# - x=-34; y=-30 -> 3

X = int(input("Введите X: "))
Y = int(input("Введите Y: "))

if X>0:
    if Y>0:
        print("1")
if X>0:
    if Y<0:
        print("2")
if X<0:
    if Y<0:
        print("3")
if X<0: 
    if Y>0:
        print("4")