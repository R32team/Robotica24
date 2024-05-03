import socket


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
            self.start_lego_cart()

    def start_lego_cart(self):
#qua bisognava mettere il codice lego ma siamo nella *****

    #asyncio.run(line_follow_to_object())

        print("Fine esecuzione")

if __name__ == '__main__':
    server = LegoCartServer(host='0.0.0.0', port=5008)
    server.start_server()