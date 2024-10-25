import socket

class MyClient:
    def __init__(self, host, port):
        self.host = host
        self.port = port
        self.sock = None

    def connect_to_server(self):
        try:
            self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            self.sock.connect((self.host, self.port))
            print(f"Connected to the server at {self.host}:{self.port}")
        except socket.error as e:
            print(f"Connection error: {e}")

    def communicate(self):
        try:
            while True:
                message = input("Client: ")
                if message.lower() == 'stop':
                    break
                self.sock.sendall(message.encode('utf-8'))
                server_message = self.sock.recv(1024).decode('utf-8')
                print(f"Server says: {server_message}")
        except socket.error as e:
            print(f"I/O error: {e}")
        finally:
            self.close_connection()

    def close_connection(self):
        if self.sock:
            self.sock.close()
            print("Connection closed")

if __name__ == "__main__":
    client = MyClient("192.168.178.59", 7777)  
    client.connect_to_server()
    client.communicate()