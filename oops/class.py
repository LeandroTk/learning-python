# -*- coding: utf-8 -*-

# 1º exemplo de classe
class MyFirstClass:
	pass

Objeto1 = MyFirstClass()
Objeto2 = MyFirstClass()

print(Objeto1)
# <__main__.MyFirstClass object at 0xb7b7faec>
print(Object2)
# <__main__.MyFirstClass object at 0xb7b7fbac>

# -------------------- Atributos -------------------------

class Point1:
	pass

p1 = Point1()
p2 = Point1()

# <objeto>.<atributo> = <valor>
p1.x = 5
p1.y = 4

# <objeto>.<atributo> = <valor>
p2.x = 3
p2.y = 6

# --------------------- Métodos --------------------------

class Point2:
	def reset(self):
		self.x = 0
		self.y = 0

p = Point2()

# <objeto>.<método>
p.reset()
print(p.x, p.y)

# --------------- Múltiplos Argumentos -------------------

import math

class Point3:
	def move(self, x, y):
		self.x = x
		self.y = y

	def reset(self):
		self.move(0, 0)

	def calculate_distance(self, other_point):
		return math.sqrt((self.x - other_point.x) ** 2 + (self.y - other_point.y) ** 2)

point1 = Point3()
point2 = Point3()

point1.reset()
point2.move(5, 0)

# Utilizando os dois objetos e o método calculate_distance, que vai calcular a distância entre esses dois pontos criados.
print(point1.calculate_distance(point2))