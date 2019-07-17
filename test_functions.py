
#Exercise 3,3
#Arnaldo Jr
import time
from robot_control_class import RobotControl #importa uma classe
robotcontrol = RobotControl() #criando um objeto


def robotmove(a,b,c):
#    print('executando acao 1...',a,b,c)
    resultado = robotcontrol.move_straight_time(a,b,c)
    print(resultado)

def robotturn(a,b,c):
#    print('executando acao 2...',+a,+b,+c)
    resultado = robotcontrol.turn(a,b,c)
    print(resultado)
fim = "nao"
while fim != "sim":
    a = raw_input('direcao: forward ou backward ')
    b = input('velocidade: m/s ')
    c = input('tempo: seg ')
    robotmove(a,b,c)
    print('funcao turn')
    d = raw_input('clockwise: ')
    b = input('velocidade: m/s ')
    c = input('tempo: seg ')
    robotturn(d,b,c)
    fim = raw_input("finalizado?")