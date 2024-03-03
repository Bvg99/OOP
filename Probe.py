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


class SomeClass:
    x = 67

    def __init__(self):
        self.x = 78
    def method_one(self):
        x = 23
        print('method_one, x = ', x)

    def method_two(self):
        x = 34
        def func():
            x = 56
            print('func, x = ', SomeClass.x)
        func()
        print('method_two, x = ', self.x)

x = 12
obj = SomeClass()
obj.method_one()
obj.method_two()
print('global ', x)





