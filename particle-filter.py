import numpy as np
import random
from math import *

random.seed(3)

round_num = 2
world_size = 100.0
num_of_robots = 1000
landmark = [[0, 0],
            [world_size, 0],
            [0, world_size],
            [world_size, world_size]]


class Robot:
    def __init__(self):
        self.x = random.random() * world_size
        self.y = random.random() * world_size
        self.ori = random.random() * (2.0 * np.pi)

    def set(self, new_x, new_y, new_ori):
        self.x = new_x % world_size
        self.y = new_y % world_size
        self.ori = new_ori % (2.0 * np.pi)

    def move(self, turn, steps):
        self.set(self.x, self.y, self.ori + turn)
        self.set(self.x + (cos(self.ori)*steps),
                 self.y + (sin(self.ori)*steps), self.ori)

    def sense(self):
        result = []
        for i in landmark:
            result.append(sqrt(((i[0]-self.x)**2) +
                               ((i[1]-self.y)**2)))

            # result.append(round(sqrt(((i[0]-self.x)**2)+
            #                    ((i[1]-self.y)**2)), round_num))
        return result

    def print(self):
        print("[ x =", round(self.x, round_num),
              ", y =", round(self.y, round_num),
              ", heading =", round(self.ori, round_num), "]")

    def gaussian(self, mu, sigma2, x):
        # calculates the probability of x for 1-dim Gaussian with mean mu and var. sigma
        return (1/sqrt(2.*pi*sigma2))*exp((-1/2)*((x-mu)**2)/sigma2)

    # def measurement_prob(self, measurement):
    #     # calculates how likely a measurement should be
    #     prob = 1.0
    #     for i in range(len(landmark)):
    #         dist = sqrt(((self.x - landmark[i][0]) ** 2) +
    #                     (self.y - landmark[i][1]) ** 2)
    #         prob *= self.gaussian(dist, 0.05**2, measurement[i])
    #     return prob

    def measurement_prob(self, measurement):
        # calculates how likely a measurement should be
        prob = 1.0
        for i in range(len(landmark)):
            dist = sqrt(((self.x - landmark[i][0]) ** 2) +
                        (self.y - landmark[i][1]) ** 2)
            prob *= self.gaussian(dist, 0.05**2, measurement[i])
        return prob


MyRobot = Robot()
MyRobot.set(30.0, 20.0, np.pi/2)
MyRobot.print()

robots = []
for i in range(int(num_of_robots)):
    robots.append(Robot())
for rob in robots:
    rob.print()


Myfirstdistance = MyRobot.sense()
firstdistance = []
for rob in robots:
    firstdistance.append(rob.sense())

print(Myfirstdistance)
print(firstdistance)


MyRobot.print()
print(MyRobot.sense())


# MyRobot.move(pi/2, 15)
# MyRobot.print()
# print(MyRobot.sense())
#
#
# MyRobot.move((np.pi/3), 10)
# MyRobot.print()
# print(MyRobot.sense())
#
# for rob in robots:
#     # rob.move(np.pi/2, 15)
#     rob.move(6*pi, 5)
#
print(firstdistance[0])
print(robots[0].sense())
print("*****")
#print(MyRobot.measurement_prob(MyRobot.sense()))
#print(robots[0].measurement_prob(MyRobot.sense()))
MyRobot.print()


def gaussian(mu, sigma2, x):
    # calculates the probability of x for 1-dim Gaussian with mean mu and var. sigma
    return (1/sqrt(2.*pi*sigma2))*exp((-1/2)*((x-mu)**2)/sigma2)


# wight = []
# for rob_dist in firstdistance:
#     print("~~~~~")
#     print(firstdistance.index(rob_dist), "/", len(firstdistance))
#     print(rob_dist)
#     prob = 1.0
#     for i in range(len(landmark)):
#         print(rob_dist[i], "~~", Myfirstdistance[i])
#         print("~",prob,"~~", gaussian(rob_dist[i], 0.5**2, Myfirstdistance[i]))
#         prob *= gaussian(rob_dist[i], 0.5**2, Myfirstdistance[i])
#         print("***************", prob)
#     print("*", prob)
#     wight.append(prob)

wight = []
for rob_dist in firstdistance:
    prob = 1.0
    for i in range(len(landmark)):
         prob *= gaussian(rob_dist[i], 0.5**2, Myfirstdistance[i])
    wight.append(prob)

print(wight.index(max(wight)))
print(wight)


def normalizewight(wight):
    sw = sum(wight)
    for i in range(len(wight)):
        wight[i] /= sw

normalizewight(wight)
print(wight)

