# Aluno: Pedro Wilson Rodrigues de Lima.
# Nº de Matrícula: 2020267.

import socket

def main():

    host = 'localhost'
    port = 12345


    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)


    server_socket.bind((host, port))

    server_socket.listen(1)

    print('Servidor em execução...')

    client_socket, addr = server_socket.accept()
    print('Cliente conectado:', addr)

    while True:

        message = client_socket.recv(1024).decode()
        if not message:
            break

        print('Mensagem recebida do cliente:', message)


    client_socket.close()

if __name__ == '__main__':
    main()
