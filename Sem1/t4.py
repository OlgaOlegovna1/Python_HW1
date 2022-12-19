# Напишите программу, которая принимает на вход координаты двух точек 
# и находит расстояние между ними в 2D пространстве.

# Пример:

# - A (3,6); B (2,1) -> 5,09
# - A (7,-5); B (1,-1) -> 7,21

Xa = int(input("Введите координаты точки А: "))
Ya = int(input())
Xb = int(input("Введите координаты точки B: "))
Yb = int(input())

distance = ((Xb - Xa)*(Xb - Xa) + (Yb - Ya)*(Yb - Ya))
import math
sqrt = math.sqrt(distance)
print(sqrt)