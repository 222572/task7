import socket
import threading


def handle_client(client_socket, client_address):
    print(f"Подключен клиент: {client_address}")
    
    data = client_socket.recv(1024)
    print(f"Получены данные: {data.decode()}")
    client_socket.sendall(data)

    client_socket.close()

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server_socket.bind(('localhost', 12345))

server_socket.listen(5)
print("Сервер слушает порт 12345...")

while True:
    client_socket, client_address = server_socket.accept()

    client_thread = threading.Thread(target=handle_client, args=(client_socket, client_address))
    client_thread.start()
