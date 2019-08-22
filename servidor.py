# ********************************************
# Autor: Fernando Krein Pinheiro
# Data: 12/05/2012
# Linguagem: Python
# ========= IMPORTANTE ===========
# O código esta livre para usar,
# citar e compartilhar desde que
# mantida sua fonte e seu autor.
# Obrigado.
#
# Código fonte baseado nos originais
# de Marcio Minicz encontrado em:
# http://www.python.org.br/wiki/SocketBasico
#
# ********************************************

import socket
import _thread
import os
import serial

HOST = ''
PORTA = 10002
PORTA_SERIAL = '/dev/ttyACM0'
BAUD_RATE = 9600

conSerial = serial.Serial(PORTA_SERIAL, BAUD_RATE)
os.system("clear")

print("teste")


def conecta(conexao, cliente):
    print("IP conectado | Porta", cliente)

    while True:
        dados = conexao.recv(1024)
        if not dados: break
        print("Cliente para Arduino: ", dados.decode('utf-8'))
        conSerial.write("i".encode('utf-8')+dados+"\n".encode('utf-8'))
        mensagem = conSerial.readline().decode('utf-8')
    print("Arduino Diz: ", mensagem)

    print('Cliente encerrou conexao', cliente)
    print("Terminando...")
    conSerial.close()
    conexao.close()
    _thread.exit()
    _thread.sys.exit()


tcpSOCKET = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
conexaoORIGEM = (HOST, PORTA)
tcpSOCKET.bind(conexaoORIGEM)
tcpSOCKET.listen(1)

print("teste2")
while True:
    conexao, cliente = tcpSOCKET.accept()
    _thread.start_new_thread(conecta, tuple([conexao, cliente]))

tcpSOCKET.close()

