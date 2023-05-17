# Aluno: Pedro Wilson Rodrigues de Lima.
# Nº de Matrícula: 2020267.

import socket

def main():

    host = 'localhost'
    port = 12345

    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    client_socket.connect((host, port))

    while True:

        message = input('Digitar a mensagem a ser enviada ao servidor: ')

        client_socket.send(message.encode())

        if message.lower() == 'sair':
            break

    client_socket.close()

if __name__ == '__main__':
    main()
