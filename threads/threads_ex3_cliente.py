import socket
import threading

HOST = '127.0.0.1'
PORT = 8080
BUFFER = 1024



def receber():
    while True:
        try:
            mensagem = cliente_servidor.recv(BUFFER).decode()
            print(mensagem)
        except Exception as error:
            print(f'Erro --> {error}')
            break

cliente_servidor = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
cliente_servidor.connect((HOST, PORT))

threading.Thread(name="Cliente_Servidor", 
                 target=receber,
                 daemon=True).start()

while True:
    msg = str(input('\nDigite a mensagem: '))
    if msg.lower == 'sair':
        break
    cliente_servidor.send(msg.encode())

cliente_servidor.close()