'''Python 3.7'''
import json
import random
import socket
import string

# Increase this value exponentially to self.num_messages
BUFFER_SIZE = 1024000

class Producer():
    """TCP Client Class"""

    # Useful connection constraints
    HOST = '127.0.0.1'  # Standard loopback interface address (localhost)
    PORT = 65432        # Port to listen on (non-privilege ports are > 1023)

    def __init__(self, num=1000):
        self.num_messages = num
        self.messages = {}

    def open_connection(self, h=HOST, p=PORT):
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.connect((h, p))
            self.generate_messages()
            s.sendall(json.dumps(self.messages).encode('utf-8'))
            data = s.recv(BUFFER_SIZE)

        print('Received', repr(data))

    def generate_messages(self):
        '''
        Generates a configurable number of messages (default 1000) to random phone numbers.
        '''
        msg = ''    # Variable to store each unique message
        num = ''    # Variable to store each unique phone number
        chars = string.ascii_letters + string.digits + string.punctuation   # Fills msg
        digits = string.digits                                              # Fills num
        # Dictionary update loop
        #   range of self.num_messages+1 to account for end condition
        for i in range(self.num_messages+1):
            # Only update once at least one random message and number have been generated
            if (msg != num): self.messages[num]=msg
            # Reset variables after each loop
            msg = ''
            num = ''
            # Random message generation loop
            #   range of 100 according to problem specifications
            for j in range(100):
                msg += random.choice(chars)
            # Random number generation loop
            #   range of 10 to account for U.S. phone number limits
            for k in range(10):
                num += random.choice(digits)

def main():
    p = Producer()
    p.open_connection()

if __name__ == "__main__":
    main()
