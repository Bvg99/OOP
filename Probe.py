# admins = []
# for user in get_users():
#     if user.is_admin:
#         admins.append(user)
#
#
# def get_users():
#     for user in range (5):
#         print(user)
#
# get_users()
from random import randint

from termcolor import cprint

# admins = [user for user in get_users() if user.is_admin]


# my_list = [1, 2, 3]
# my_list.append([[88, 89], [95, 96, 98]])
# # my_list.extend([[88, 88], [88, 88, 88]])
# my_list.extend([88, 88])
# print(my_list)
#
# # my_list.remove(88)
# print(my_list)
#
# while 88 in my_list:
#     my_list.remove(88)
#
# print(my_list)


values = ['gold', 'silver', 'palladium', 'platinum']


# class Tainik:
#     def __init__(self, item=None):
#         self.content = []
#         if item is not None:
#             self.content.append(item)
#     def put(self, value):
#         self.content.extend(value)
#         print('added ', value)
#         print(self.content)
#
#
# tainik = Tainik()
#
# tainik.put(values[2])
#
# print(len(self))


# class SomeClass:
#     x = 67
#
#     def __init__(self):
#         self.x = 78
#     def method_one(self):
#         x = 23
#         print('method_one, x = ', x)
#
#     def method_two(self):
#         x = 34
#         def func():
#             x = 56
#             print('func, x = ', SomeClass.x)
#         func()
#         print('method_two, x = ', self.x)
#
# x = 12
# obj = SomeClass()
# obj.method_one()
# obj.method_two()
# print('global ', x)


# class Man:
#
#     def __init__(self, name):
#         self.name = name
#         self.fullness = 50
#         self.food = 50
#         self.money = 0
#
#     def __str__(self):
#         #return 'I am {}, my fullness: {}, the rest of food: {}, the rest of money: {}'.format(
#         #    self.name, self.fullness, self.food, self.money)
#
#         return (f'I am {self.name}, my fullness: {self.fullness}, '
#                 f'the rest of food: {self.food}, the rest of money: {self.money}')
#
#     def eat(self):
#         if self.food >= 10:
#             print('{} has eaten'.format(self.name))
#             self.fullness += 10
#             self.food -= 10
#         else:
#             print(f'no food for {self.name}')
#
#     def work(self):
#         print(f'{self.name} has worked')
#         self.money += 50
#         self.fullness -= 10
#
#     def play_DOTA(self):
#         print(f'{self.name} was playing DOTA all day long')
#         self.fullness -= 10
#
#     def buy_food(self):
#         if self.money >= 10:
#             print(f'{self.name} bought food')
#             self.food += 10
#             self.money -= 20
#         else:
#             print(f'no money for {self.name}')
#
#     def act(self):
#         if self.food < 30:
#             self.buy_food()
#         if self.fullness < 20:
#             self.eat()
#         if self.money <=50:
#             self.work()
#         dice = randint(1, 6)
#         print('dice ', dice)
#         if dice == 1:
#             self.work()
#         elif dice == 2:
#             self.eat()
#         else:
#             self.play_DOTA()
#
#
# vasya = Man('Vasya')
# leon = Man('leon')
#
# for day in range(1, 21):
#     cprint('================ day {} ================'.format(day), color='yellow')
#     vasya.act()
#     leon.act()
#     print(vasya)
#     print(leon)


class Person:
   def __init__(self, name, age):
      self.name = name
      self.age = age

   def __eq__(self, other):
      # if isinstance(other, Person):
      return self.name == other.name and self.age == other.age
      # return False

p1 = Person("John", 30)
#p2 = Person("John", 30)
p2 = 30
if p1 == p2:
   print("p1 and p2 are equal")
else:
   print('no')