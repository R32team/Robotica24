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
        from hub import port
        '''import motor_pair
        import color_sensor
        import distance_sensor
        import color'''
        import asyncio
        import time


        #--oggetti
        print("Definisco oggetti")
        motor_pair.pair(motor_pair.PAIR_1, port.C, port.D)

        #--funzioni
        print("Definisco funzione")
        async def line_follow_to_object():
            Kp = 1.5
            print("Inizio movimento motori")
            motor_pair.move(motor_pair.PAIR_1, 70)
            termina_programma = False
            while not termina_programma:
                if color_sensor.color(port.A) is color.YELLOW:
                    Kp = -1.5
                if color_sensor.color(port.A) is color.GREEN:
                    Kp = 1.5
                distance = distance_sensor.distance(port.B)
                #print("Distance =", distance/10, "cm")
                #print("Oggetto raggiunto?")
                if distance == -1:
                    distance = 2000
                if distance < 200:
                    motor_pair.stop(motor_pair.PAIR_1)
                    time.sleep(2)
                    continue
                #print("Distance =", distance)
                if color_sensor.color(port.A) is color.AZURE:
                    termina_programma = True
                    print("Azzurro rilevato")
                    break
                else:
                    reflectedlight = color_sensor.reflection(port.A)
                    error = 50 - reflectedlight
                    control_output = int(Kp * error)
                    #print("Control output = ", control_output)
                    motor_pair.move(motor_pair.PAIR_1, control_output)
            motor_pair.stop(motor_pair.PAIR_1)
        print("Funzione definita")

        #--execute
        print("Inizio esecuzione")

        asyncio.run(line_follow_to_object())

        print("Fine esecuzione")

if __name__ == '__main__':
    server = LegoCartServer(host='0.0.0.0', port=5008)
    server.start_server()