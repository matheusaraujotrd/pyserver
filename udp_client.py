import socket
import sys
import udp_server

def main():
    try:
        connection = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    except socket.error as udp_socket_error:
        print("O cliente TCP falhou")
        print(f"Erro {udp_socket_error}")
    print("Socket criado.")

    host = "localhost"
    msg = "Cliente: Mensagem enviada pelo cliente"

    try:
        connection.sendto(msg.encode(), (host, 5432))
        data, server = connection.recvfrom(4096)
        data = data.decode()

    except socket.error as udp_connection_error:
        print("A conexão TCP falhou")
        print(f"Erro {udp_connection_error}")
        sys.exit()
    finally:
        print(data)
        connection.close()
        print("Encerrando conexão UDP.")


if __name__ == "__main__":
    main()
