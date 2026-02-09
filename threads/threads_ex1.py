'''
Thread é uma linha de execução dentro de um mesmo programa.
- Provessor --> programa inteiro.
- Thread --> tarefas que rodam 'ao mesmo tempo' dentro do processo.

--Sem Threads--
-Cliente A conecta --> Espera terminar.
-Cliente B conecta --> Espera A.
-Cliente C conecta --> Espera B.

--Com Threads--
-Cliente A,B,C --> Atendidos ao mesmo tempo.

'''

import threading
import time

def tarefa():
    for i in range(5):
        print(f'Executando tarefa.... {i}')
        time.sleep(i)
    
thread = threading.Thread(target=tarefa) # Target == Funão que a Thread vai executar.
thread.start() # Inicia Thread
thread.join() # O programa só finaliza depois que a função da Thread for executada.

def atender_cliente(nome):
    print(f'Atendendo cliente: {nome}')

clientes = ['Ana', 'João', 'Carlos']

for clientes in clientes:
    t = threading.Thread(target=atender_cliente, args=(clientes,)) # args(clientes, ) --> a virgula é obrigatoria.
    t.start()

print('Programa principal continua....')
