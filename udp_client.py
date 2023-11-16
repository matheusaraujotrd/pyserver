import socket
import sys


def main():
    try:
        connection = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    except socket.error as udp_socket_error:
        print("O cliente TCP falhou")
        print(f"Erro {udp_socket_error}")
    print("Socket criado.")

    host = "localhost"
    port = 5433
    msg = "Testing successful"

    try:
        print("Cliente:" + msg)
        connection.sendto(msg.encode(), (host, 5432))

        data, server = connection.recvfrom(4096)
        data = data.decode()
        print("Recebido: " + data)
    except socket.error as udp_connection_error:
        print("A conexão TCP falhou")
        print(f"Erro {udp_connection_error}")
        sys.exit()
    finally:
        connection.close()
        print("Encerrando conexão UDP.")