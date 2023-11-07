# class Point:
#
#     def __new__(cls, *args, **kwargs):
#         print('wethod new')
#         return super().__new__(cls)
#
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y
#
# p = Point(2, 8)
# # print(p.__dict__)
# print(p.x)
import random
# class DataBase:
#     __instance = None
#
#     def __new__(cls, *args, **kwargs):
#         if cls.__instance is None:
#             cls.__instance = super().__new__(cls)
#         return cls.__instance
#
#     def __init__(self, user, password, port):
#         self.user = user
#         self.password = password
#         self.port = port
#
#     def __del__(self):
#         print('Error')
#         DataBase.__instance = None
#
#     def connect(self):
#         print(f'Соединение с БД: {self.user}, {self.password}, {self.port}')
#
#     def close(self):
#         print('Соединение прервано')
#
#     def read(self):
#         print('Чтение данных')
#
#     def write(self, data):
#         print(f'Записываем данные: {data}')
#
# db = DataBase('user1', 'pws1', '8800')
# db2 = DataBase('user1', 'pws1', '8800')
# db.connect()
# print(db)
# print(db2)

# class Test:
#
#     # def __repr__(self):
#     #     return 'Object Test'
#
#     def __init__(self, name):
#         self.name = name
#
#     def __str__(self):
#         return f'Наименование товара'
#
# t = Test('comp')
# t2 = Test('phone')
# print(t.name)
# print(t2)

# class Test2:
#     pass
#     def __bool__(self):
#         # return 2 < 6
#         return True
# t = Test2()
#
# if t:
#     print('oject')

# class Clock:
#     __Day = 86400
#     def __init__(self, seconds : int):
#         if not isinstance(seconds, int):
#             raise TypeError('Нужно ввести целое число')
#         self.seconds = seconds % self.__Day
#
#     def get_time(self):
#         s = self.seconds % 60
#         m = self.seconds // 60 % 60
#         h = self.seconds // 3600 % 24
#         return f'{h} : {m} : {s}'
#
#     def __eq__(self, other):
#         if not isinstance(other, (int, Clock)):
#             raise TypeError('Нужно ввести целое число')
#         # if isinstance(other, int):
#         #     other = other
#         # else:
#         #     other = other.seconds
#         sc = other if isinstance(other, int) else other.seconds
#         return self.seconds == sc
#
#     def __lt__(self, other):
#         if not isinstance(other, (int, Clock)):
#             raise TypeError('Type Error')
#         sc = other if isinstance(other, int) else other.seconds
#         return self.seconds <= sc
#
#     def __add__(self, other):
#         if not isinstance(other, (int, Clock)):
#             raise ArithmeticError('Не можем сложить ')
#         sc = other if isinstance(other, int) else other.seconds
#         return Clock(self.seconds + sc)
#
#     def __iadd__(self, other):
#         if not isinstance(other, (int, Clock)):
#             raise ArithmeticError('Не можем сложить ')
#         sc = other if isinstance(other, int) else other.seconds
#         return Clock(self.seconds * sc)
#
#     def __sub__(self, other):
#         if not isinstance(other, (int, Clock)):
#             raise ArithmeticError('Не можем сложить ')
#         sc = other if isinstance(other, int) else other.seconds
#         return Clock(self.seconds - sc)
#
#     # def __sul__(self, other):
#     #     if not isinstance(other, int):
#     #         raise ArithmeticError('Не можем сложить ')
#     #     return Clock(self.seconds * other)
# cl = Clock(86401)
# cl2 = Clock(86400)
# # print(cl.seconds)
# # print(cl)
# # print(cl2)
# # print(cl < cl2)
# print(cl.get_time())
# cl = cl * 3
# print(cl.get_time())

# class Password:
#     def __init__(self, first_name, last_name, country, data_ot_birth, num_og_passport):
#         self.first_name = first_name
#         self.last_name = last_name
#         self.country = country
#         self.data_ot_birth = data_ot_birth
#         self.num_og_passport = num_og_passport
#
#     def printInfo(self):
#         print(f'''
# Full name: {self.first_name} {self.last_name}
# Data of Birth: {self.data_ot_birth}
# Country: {self.country}
# Passport: {self.num_og_passport}
# ''')
#     def __repr__(self):
#         return f'name: {self.first_name} {self.last_name}, Passport: {self.num_og_passport}'
#
#
# class ForeighPassport(Password):
#     def __init__(self, first_name, last_name, country, data_ot_birth, num_og_passport, visa):
#         super().__init__(first_name, last_name, country, data_ot_birth, num_og_passport)
#         self.visa = visa
#
#     def printInfo(self):
#         super().printInfo()
#         print('Visa:', self.visa)
#
# MFC = []
# p = Password('Tyui', 'Ttrewrt', 'Russia', '14.05.2005', '0987 567899')
# # p.printInfo()
# MFC.append(p)
# fp = ForeighPassport('Petr', 'Timerkaev', 'Russia', '12.09.1997', '9876 3456786', 'China')
# # fp.printInfo()
# MFC.append(fp)
# print(MFC)
# for item in MFC:
#     item.printInfo()

# class Equipment:
#     def __init__(self, name, make, year):
#         self.name = name
#         self.make = make
#         self.year = year
#
#     def action(self):
#         return 'не определено'
#     def __str__(self):
#         return f'{self.name}, {self.make}, {self.year} Умеет "{self.action()}"'
#
#     def __le__(self, other):
#         if not isinstance(other, Equipment):
#             raise TypeError
#         return self.year <= other.year
# class Printer(Equipment):
#     def __init__(self, series, name, make, year):
#         super().__init__(name, make, year)
#         self.series = series
#
#     def action(self):
#         return 'печатает с ПК на листочек'
#     def __str__(self):
#         return f'{self.series}, {self.name}, {self.make}, {self.year}  Умеет "{self.action()}"'
#
# class Scaner(Equipment):
#     def __init__(self, name, make, year):
#         super().__init__(name, make, year)
#
#     def action(self):
#         return 'сканирует в ПК'
#
# class Xerox(Equipment):
#     def __init__(self, name, make, year):
#         super().__init__(name, make, year)
#
#     def action(self):
#         return 'копирует и печатает на листочек'
#
# def allItems(sklad):
#     for item in sklad:
#         print(item)
# def get_items(sklad, ename):
#     for item in sklad:
#         if isinstance(item, ename):
#             print(item)
# sklad = []
# e = Equipment('Noname', 'XxX', 2000)
# sklad.append(e)
# s = Printer('98765','cvhj', 'lvnml', 2009)
# x = Xerox('hfgd', 'fghdsa', 2345)
# sklad.append(s)
# sklad.append(x)
# get_items(sklad, Equipment)

# from random import randint
# class Soldier:
#      def __init__(self, name='Noname', health = 100):
#          self.name = name
#          self.health = health
#      def set_name(self, name):
#          self.name = name
#      def make_kick(self, enemy):
#         enemy.health -= random.randint(15, 20)
#         if enemy.health < 0:
#             enemy.health = 0
#         self.health += random.randint(5, 10)
#         print(self.name, "бьет", enemy.name)
#         print('%s = %d' % (enemy.name, enemy.health))
#
# class Battle:
#     def __init__(self, u1, u2):
#         self.u1 = u1
#         self.u2 = u2
#         self.result = "Сражения не было"
#
#     def battle(self):
#         while self.u1.health > 0 and self.u2.health > 0:
#             n = randint(1, 2)
#             if n == 1:
#                 self.u1.make_kick(self.u2)
#             else:
#                 self.u2.make_kick(self.u1)
#         if self.u1.health > self.u2.health:
#             self.result = self.u1.name + " ПОБЕДИЛ"
#         elif self.u2.health > self.u1.health:
#             self.result = self.u2.name + " ПОБЕДИЛ"
#     def who_win(self):
#        print(self.result)
#
#
# first = Soldier('Mr. First',140)
# second = Soldier()
# second.set_name('Mr. Second')
# b = Battle(first, second)
# b.battle()
# b.who_win()

# import random
# class Card():
#     NumsList = ["Джокер", '2', '3', '4', '5', '6', '7', '8', '9', '10', "Валет", "Дама", "Король", "Туз"]
#     MastList = ["пик", "крестей", "бубей", "червей"]
#     def __init__(self, i, j):
#         self.Mastb = self.MastList[i - 1]
#         self.Num = self.NumsList[j - 1]
#
# class DeckOfCards():
#     def __init__(self):
#         self.deck = [None] * 56
#         k = 0
#         for i in range(1, 4 + 1):
#             for j in range(1, 14 + 1):
#                 self.deck[k] = Card(i, j)
#                 k += 1
#     def shuffle(self):
#         random.shuffle(self.deck)
#     def get(self, i):
#         if 0 <= i <= 55 :
#             answer = self.deck[i].Num
#             answer += " "
#             answer += self.deck[i].Mastb
#         else :
#             answer = "В колоде только 56 карт"
#         return answer
#
# deck = DeckOfCards()
# deck.shuffle()
# print('Выберите карту из колоды в 56 карт:');
# n = int(input())
# if n <= 56:
#     card = deck.get(n - 1)
#     print('Вы взяли карту: ', card, end='.\n')
# else:
#     print("В колоде только 56 карт")

# class Vector3D:
#     def __init__(self, x=0, y=0, z=0):
#         self.x = x
#         self.y = y
#         self.z = z
#
#     def display(self):
#         print(f"({self.x}, {self.y}, {self.z})")
#
#     def __add__(self, other):
#         return Vector3D(self.x + other.x, self.y + other.y, self.z + other.z)
#
#     def __sub__(self, other):
#         return Vector3D(self.x - other.x, self.y - other.y, self.z - other.z)
#
#     def __mul__(self, other):
#         if isinstance(other, Vector3D):
#             return self.x * other.x + self.y * other.y + self.z * other.z
#         elif isinstance(other, (int, float)):
#             return Vector3D(self.x * other, self.y * other, self.z * other)
#
#     def __matmul__(self, other):
#         return Vector3D(self.y * other.z - self.z * other.y,
#                         self.z * other.x - self.x * other.z,
#                         self.x * other.y - self.y * other.x)
#
#     def read(self):
#         self.x = float(input("Введите x: "))
#         self.y = float(input("Введите y: "))
#         self.z = float(input("Введите z: "))
#
#
# v1 = Vector3D(4, 1, 2)
# v1.display()
# v2 = Vector3D()
# v2.read()
# v3 = Vector3D(1, 2, 3)
# v4 = v1 + v2
# v4.display()
# a = v4 * v3
# print(a)
# v4 = v1 * 10
# v4.display()
# v4 = v1 @ v3
# v4.display()

# import math
# class RightTriangle:
#
#     def __init__(self, a, b):
#         self.a = a
#         self.b = b
#         self.c = math.sqrt(a**2 + b**2)
#
#     def increase_side(self, percent):
#         self.a *= (1 + percent/100)
#         self.b *= (1 + percent/100)
#         self.c = math.sqrt(self.a**2 + self.b**2)
#
#     def decrease_side(self, percent):
#         self.a *= (1 - percent/100)
#         self.b *= (1 - percent/100)
#         self.c = math.sqrt(self.a**2 + self.b**2)
#
#     def calculate_circumradius(self):
#         return self.c / 2
#
#     def calculate_perimeter(self):
#         return self.a + self.b + self.c
#
#     def calculate_angles(self):
#         alpha = math.degrees(math.asin(self.a / self.c))
#         beta = math.degrees(math.asin(self.b / self.c))
#         gamma = 90
#         return alpha, beta, gamma
#
# triangle = RightTriangle(3, 4)
# print("Исходный треугольник:")
# print(f"Сторона a: {triangle.a}")
# print(f"Сторона b: {triangle.b}")
# print(f"Сторона c (гипотенуза): {triangle.c}")
# print(f"\nРадиус описанной окружности: {round(triangle.calculate_circumradius(), 2)}")
# print(f"Периметр треугольника: {round(triangle.calculate_perimeter(), 2)}")
#
# angles = triangle.calculate_angles()
# print(f"\nУгол α: {round(angles[0], 2)} градусов")
# print(f"Угол β: {round(angles[1], 2)} градусов")
# print(f"Угол γ: {round(angles[2], 2)} градусов")
#
# # triangle.increase_side(10)  # Увеличиваем стороны на 10%
# # print("\nТреугольник после увеличения:")
# # print(f"Сторона a: {round(triangle.a, 2)}")
# # print(f"Сторона b: {round(triangle.b, 2)}")
# # print(f"Сторона c (гипотенуза): {round(triangle.c, 2)}")
#
# triangle.decrease_side(10)  # Уменьшение стороны на 10%
# print("\nТреугольник после уменьшения:")
# print(f"Сторона a: {round(triangle.a, 2)}")
# print(f"Сторона b: {round(triangle.b, 2)}")
# print(f"Сторона c (гипотенуза): {round(triangle.c, 2)}")


