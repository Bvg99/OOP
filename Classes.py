# # class Robot:
# #     def __init__(self):
# #         self.name = 'r2d2'
# #
# #
# #     def hello(self):
# #         print('hello, world, I am ', self.name)
# #
# #
# # robot = Robot()
# # robot.hello()
#
# # some_var = robot
# # some_var.hello()
# #
# # some_robot = some_var
# # some_robot.hello()
# #
# # some_robot.name = 'c-3po'
# # some_robot.hello()
# # robot.hello()
# # some_var.hello()
#
#
# # robot.temperature = 1
# # while robot.temperature < 10:
# #     robot.temperature *= 2
#
#
# robot_2 = Robot()
# robot_2.name = 'Vally'
#
# print(robot.name)
# print(robot_2.name)
# print(robot.name, robot_2.name)
#
# print(robot, robot_2)
#
# print(robot == robot_2, robot is robot_2)


class Backpack:
    def __init__(self, gift=None):
        self.content = []
        if gift:
            self.content.append(gift)

    def __eq__(self, other):
        return self.content == other.content

my_backpack = Backpack('butterbroad')
son_backpack = Backpack('butterbroad')

if my_backpack == son_backpack:
    print('we are so similar...')
else:
    print('we are different today!')
