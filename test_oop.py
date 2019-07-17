#!/usr/bin/env python
#Exercise 4
#Arnaldo Jr

import time
from robot_control_class import RobotControl #importa uma classe
robotcontrol = RobotControl() #criando um objeto

class Robo:

    def __init__(self):
        print("inicializando...")
        self.robotmove_motion = "forward"
        self.robotmove_speed = 5
        self.robotmove_time = 1
        self.robotturn_clockwise = "clockwise"
        self.robotturn_speed = 6
        self.robotturn_time = 2

    def robotmove(self):
        resultado = robotcontrol.move_straight_time(self.robotmove_motion, self.robotmove_speed, self.robotmove_time)
        print(resultado)

    def robotturn(self):
        resultado = robotcontrol.turn(self.robotturn_clockwise, self.robotturn_speed, self.robotturn_time)
        print(resultado)


if __name__ == '__main__':
    robo = Robo()
    robo.robotmove()
    robo.robotturn()
    robo.robotmove()