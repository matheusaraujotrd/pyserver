import socket


def main():
    connection = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    print("Socket de servidor criado")
    host = "localhost"
    port = 5432
    connection.bind((host, port))
    msg = "\nServidor: Bem-vindo(a)!"
    while 1:
        data, end = connection.recvfrom(4096)
        if data:
            print("Servidor enviando mensagem...")
            data_dec = data.decode()
            print(f"Received: {data_dec}")
            connection.sendto((msg.encode()), end)


if __name__ == "__main__":
    main()
