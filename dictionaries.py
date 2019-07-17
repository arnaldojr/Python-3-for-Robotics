from robot_control_class import RobotControl #importa uma classe
robotcontrol = RobotControl() #criando um objeto

lista_laser = robotcontrol.get_laser_full()

dicionario_laser = {}

for chave, objeto in enumerate(lista_laser):
    dicionario_laser[chave] = objeto

for i in dicionario_laser:
    print ('Posicao', i, dicionario_laser[i])