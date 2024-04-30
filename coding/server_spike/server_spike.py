import socket
from spike import PrimeHub, Motor
class LegoCartServer:
    def __init__(self, host='0.0.0.0', port=5008):
        self.host = host
        self.port = port

    def start_server(self):
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
            sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
            sock.bind((self.host, self.port))
            sock.listen()
            print(f"Server in ascolto su {self.host}:{self.port}")

            while True:
                connection, client_address = sock.accept()
                with connection:
                    print(f"Connesso a {client_address}")
                    while True:
                        data = connection.recv(1024)
                        if not data:
                            break

                        command = data.decode('utf-8')
                        if command == 'start lego cart':
                            self.start_lego_cart()
                            response = "Lego cart avviato!"
                            connection.sendall(response.encode('utf-8'))
                        else:
                            response = "Comando non riconosciuto."
                            connection.sendall(response.encode('utf-8'))

    def start_lego_cart(self):
        
#qua devi mettere il codice per la lego cart dopo aver importat quello che devi importare

        print("Avviando il Lego cart...")

if __name__ == '__main__':
    server = LegoCartServer(host='0.0.0.0', port=5008)
    server.start_server()