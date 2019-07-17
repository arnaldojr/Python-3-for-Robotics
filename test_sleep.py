
#Exercise 3,1
#Arnaldo Jr
import time
from robot_control_class import RobotControl #importa uma classe
robotcontrol = RobotControl() #criando um objeto

def robotmove(a):
    robotcontrol.move_straight()
    time.sleep(a)
    robotcontrol.stop_robot()

robotmove(5)
