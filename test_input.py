from robot_control_class import RobotControl #importa uma classe
robotcontrol = RobotControl() #criando um objeto

position = input("What's the angle position? ")

laser1 = robotcontrol.get_laser(position)

print ("The laser value received is: ", laser1)
