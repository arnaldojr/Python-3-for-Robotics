
#Exercise 3,1
#Arnaldo Jr
import time
from robot_control_class import RobotControl #importa uma classe
robotcontrol = RobotControl() #criando um objeto

laser1 = robotcontrol.get_laser(360)

while laser1 > 1:
    robotcontrol.move_straight()
    laser1 = robotcontrol.get_laser(360)
    print("distancia: ", laser1)

robotcontrol.stop_robot()
print("estou demais da parede: ")
