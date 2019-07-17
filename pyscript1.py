from robot_control_class import RobotControl #importa uma classe
robotcontrol = RobotControl() #criando um objeto

a = robotcontrol.get_laser(330)

print ("The laser value received is: ", a)