
#Exercise 3,1
#Arnaldo Jr
import time
from robot_control_class import RobotControl #importa uma classe
robotcontrol = RobotControl() #criando um objeto

def robotmove(a):
    robotcontrol.move_straight()
    time.sleep(a)
    robotcontrol.stop_robot()

print('Forneca 3 valores entre 0 e 719.')
value = [0,1,2]
value[0] = input('valor 1:')
value[1] = input('valor 2:')
value[2] = input('valor 3:')
print(value)

#robotmove(5)
laser1 = robotcontrol.get_laser(360)
print(laser1)
