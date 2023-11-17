import socket


def main():
    connection = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    print("Socket de servidor criado")
    host = "localhost"
    port = 5432
    connection.bind((host, port))
    msg = "\nServidor: Mensagem enviada pelo servidor"
    while 1:
        data, end = connection.recvfrom(4096)
        if data:
            print("Servidor enviando mensagem...")
            data = data.decode()
            connection.sendto((msg.encode()), end)
            print(f"{data}" + msg)


if __name__ == "__main__":
    main()
