from socket import socket, AF_INET, SOCK_STREAM

def run_server(host: str, port: int) -> None:
    if not isinstance(host, str) and\
        not isinstance(port, int):
        return
    
    try:
        server = socket(
            AF_INET, SOCK_STREAM
        )
        server.bind((host, port))
        server.listen(1)
        print(
            f'Сервер запущен. Начало прослушивания порта {port}...'
        )

        while True:
            client, addr = server.accept()
            print(f'Клиент подключен: {addr}')

            try:
                while True:
                    data = client.recv(1024)

                    if not data:
                        break

                    print(
                        f'Получены данные от клиента: {data.decode()}'
                    )

                    client.sendall(data)
                    print(
                        f'Отправлены данные клиенту: {data.decode()}'
                    )
            except Exception as error:
                print(
                    f'Ошибка при обработке данных: {error}'
                )
            finally:
                client.close()
                print('Клиент отключен.')

    except Exception as error:
        print(error)
    finally:
        server.close()
        print('Сервер остановлен.')

if __name__ == '__main__':
    run_server('127.0.0.1', 65432)