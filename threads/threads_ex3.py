import socket
import threading

IP = '127.0.0.1'
PORT = 8080
BUFFER = 1024

clientes = []
lock = threading.Lock()

def tratamento_clientes(conn, addrss, buffer):
    print(f'\nCliente {addrss} Conectado!')

    with lock:
        clientes.append(conn)

    try:  
        while True:
            msg_cliente = conn.recv(buffer).decode()
            if not msg_cliente:
                print(f'\nMensagem Inválida, conexão encerrada!')
                break
            
            mensagem = f'\nCliente {addrss} : {msg_cliente}'.encode()

            with lock:
                for cliente in clientes:
                    if cliente != conn:
                        cliente.send(mensagem) 

    except UnicodeError as error:
        print(f'Erro de decodificação --> {UnicodeError}')
    except ConnectionResetError as error:
        print(f"Cliente caiu abruptamente --> {ConnectionResetError}")

    finally:
        with lock:
            clientes.remove(conn)
        conn.close()
        print(f'Cliente {addrss} saiu!')

servidor_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

servidor_socket.bind((IP, PORT))
servidor_socket.listen(5)

try:
    while True:
        conn, addrss = servidor_socket.accept()
        thread = threading.Thread(name="Tratamento_Clientes", target=tratamento_clientes, args=(conn, addrss, BUFFER), daemon=True)
        thread.start()

except KeyboardInterrupt as error:
    print(f'Conexão Encerrado pelo usuário --> {error}')

finally:
    servidor_socket.close()
