
#Exercise 2.4
#arnaldo Jr
from robot_control_class import RobotControl #importa uma classe
robotcontrol = RobotControl() #criando um objeto

laser = robotcontrol.get_laser_full()
#laser = [50, 100000, 3]
lower_value = 10000
for value in laser:
    #print(value)
    if value < lower_value:
        lower_value = value
print("The lower_value is: ",lower_value)