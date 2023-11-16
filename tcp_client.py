import socket
import sys


def main():
    try:
        connection = socket.socket(socket.AF_INET, socket.SOCK_STREAM, 0)
    except socket.error as tcp_socket_error:
        print("O cliente TCP falhou")
        print(f"Erro {tcp_socket_error}")
        sys.exit()
    print("Socket criado.")

    target_host = input("Digite o IP ou host ao qual deseja se conectar: ")
    target_port = input("Digite a porta para realizar a conexão: ")

    try:
        connection.connect((target_host, int(target_port)))
        print("Cliente TCP conectado.")
        connection.shutdown(2)
    except socket.error as tcp_connection_error:
        print("A conexão TCP falhou")
        print(f"Erro {tcp_connection_error}")
        sys.exit()


if __name__ == "__main__":
    main()
