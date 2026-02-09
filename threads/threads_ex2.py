import threading
import time

#ex_1 -->
'''

def threading_nome():
    nome_threading = threading.current_thread().name
    time.sleep(2)
    print(f'\nName Thread --> {nome_threading}')
    
thread_um = threading.Thread(name="Thread_um",target=threading_nome, args=())
thread_dois = threading.Thread(name="Thread_dois", target=threading_nome, args=())
thread_tres = threading.Thread(name="Thread_tres", target=threading_nome, args=())
print('\nPrograma Finalizado --> Sincrono!')

thread_um.start()
thread_dois.start()
thread_tres.start()

thread_um.join()
thread_dois.join()
thread_tres.join()

'''

#ex_2 -->
lock = threading.Lock()

clientes = ['Fabio', 'Jorge', 'Max', 'Sonny', 'Bortoleto']
registrado = []

def imprimir_cliente(cliente):
    print(f'\n{cliente}')

def ler_cliente(cliente):
    for i in cliente:
        with lock:
            if i not in registrado:
                registrado.append(i)
                imprimir_cliente(i)
                print(f'Thread --> {threading.current_thread().name}')
        time.sleep(1)

t1 = threading.Thread(name="Threads1",target=ler_cliente, args=(clientes,))
t2 = threading.Thread(name="Threads2",target=ler_cliente, args=(clientes,))
t3 = threading.Thread(name="Threads3",target=ler_cliente, args=(clientes,))
t4 = threading.Thread(name="Threads4",target=ler_cliente, args=(clientes,))
t5 = threading.Thread(name="Threads5",target=ler_cliente, args=(clientes,))

t1.start()
t2.start()
t3.start()
t4.start()
t5.start()

t1.join()
t2.join()
t3.join()
t4.join()
t5.join()

#ex3 -->
