'''Python 3.7'''

import socket

# Increase this value exponentially to self.num_messages
BUFFER_SIZE = 1024000

class Sender():
    """TCP Server Class"""

    # Useful connection constraints
    HOST = '127.0.0.1'  # Standard loopback interface address (localhost)
    PORT = 65432        # Port to listen on (non-privilege ports are > 1023)

    def __init__(self, failure_rate, mean_time):
        self.failure_rate = failure_rate
        self.mean_time = mean_time

    def open_connection(self, h=HOST, p=PORT):
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.bind((h, p))
            s.listen()
            conn, addr = s.accept()
            with conn:
                print('Connected by', addr)
                while True:
                    data = conn.recv(BUFFER_SIZE)
                    if not data:
                        break
                    conn.sendall(data)

    def send_message(self, conn, data):
        return False

def main():
    s = Sender(1,1)
    s.open_connection()

if __name__ == "__main__":
    main()
