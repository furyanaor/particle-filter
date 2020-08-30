import numpy as np
import random

world_size = 10.0

class Robot:
    def __init__(self):  
        self.x = random.random() * world_size
        self.y = random.random() * world_size
        self.ori = random.random() * 2.0 * np.pi

    def set(self, new_x, new_y, new_ori):  
        self.x = new_x
        self.y = new_y
        self.ori = new_ori

    def bark(self):
        print("bark bark!")

MyRobot = Robot()
MyRobot.set(12, 2, np.pi)
print("[ x =", round(MyRobot.x, 2), ", y =", round(MyRobot.y, 2), ", heading =", round(MyRobot.ori, 2), "]")

robots = []
for i in range(int(world_size)):
    robots.append(Robot())
for rob in robots:
    print("[ x =", round(rob.x, 2), ", y =", round(rob.y, 2), ", heading =", round(rob.ori, 2), "]")
