import socket

class MyServer:
    def __init__(self, host='192.168.0.171', port=6666):
        self.host = host
        self.port = port
        self.server_socket = None
        self.client_socket = None

    def start_server(self):
        try:
            # Create a TCP/IP socket
            self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            self.server_socket.bind((self.host, self.port))
            self.server_socket.listen(1)  # Listen for incoming connections
            print(f"Server started, waiting for client to connect on {self.host}:{self.port}...")

            # Accept a connection
            self.client_socket, client_address = self.server_socket.accept()
            print(f"Client connected from {client_address}")

            self.communicate()

        except socket.error as e:
            print(f"Socket error: {e}")
        finally:
            self.close_server()

    def communicate(self):
        try:
            while True:
                # Receive the message from the client
                client_message = self.client_socket.recv(1024).decode('utf-8')

                # If the client sends "CLOSE SOCKET", break the loop and close the connection
                if client_message.strip().upper() == 'CLOSE SOCKET':
                    print("Client requested to close the connection.")
                    break

                # Capitalize the message and send it back to the client
                capitalized_message = client_message.upper()
                print(f"Client says: {client_message}")
                self.client_socket.sendall(capitalized_message.encode('utf-8'))

        except socket.error as e:
            print(f"I/O error: {e}")
        finally:
            self.close_connection()

    def close_connection(self):
        if self.client_socket:
            self.client_socket.close()
            print("Client socket closed")

    def close_server(self):
        if self.server_socket:
            self.server_socket.close()
            print("Server socket closed")

if __name__ == "__main__":
    server = MyServer()  
    server.start_server()
