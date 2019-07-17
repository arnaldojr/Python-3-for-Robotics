from robot_control_class import RobotControl #importa uma classe
robotcontrol = RobotControl() #criando um objeto

laser1 = robotcontrol.get_laser(360)

print ("The laser1 value received is: ", laser1)

laser2 = robotcontrol.get_laser(330)

print ("The laser2 value received is: ", laser2)

laser2 = robotcontrol.get_laser(370)

print ("The laser2 value received is: ", laser2)