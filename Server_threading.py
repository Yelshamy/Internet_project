import socket
import threading

class MyServer:
    def __init__(self, host='192.168.178.59', port=7777):
        self.host = host
        self.port = port
        self.server_socket = None
        self.clients = {}  # Dictionary to store client information

    def start_server(self):
        try:
            # Create a TCP/IP socket
            self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            self.server_socket.bind((self.host, self.port))
            self.server_socket.listen(5)  # Allows up to 5 queued connections
            print(f"Server started, waiting for clients to connect on {self.host}:{self.port}...")

            while True:
                client_socket, client_address = self.server_socket.accept()                    # Accept a new client connection
                print(f"Client connected from {client_address}")

                # Save client information
                self.clients[client_address] = {
                    'socket': client_socket,
                    'address': client_address
                }

                # Start a new thread to handle this client
                client_thread = threading.Thread(target=self.handle_client, args=(client_socket, client_address))
                client_thread.start()

        except socket.error as e:
            print(f"Socket error: {e}")
        finally:
            self.close_server()

    def handle_client(self, client_socket, client_address):
        try:
            while True:
                client_message = client_socket.recv(1024).decode('utf-8')


                if client_message.strip().upper() == 'CLOSE SOCKET':
                    print(f"Client {client_address} requested to close the connection.")
                    break


                capitalized_message = client_message.upper()
                print(f"Client {client_address} says: {client_message}")
                client_socket.sendall(capitalized_message.encode('utf-8'))

        except socket.error as e:
            print(f"I/O error with client {client_address}: {e}")
        finally:
            # Remove client info and close connection
            self.close_connection(client_socket, client_address)

    def close_connection(self, client_socket, client_address):
        if client_address in self.clients:
            del self.clients[client_address]  # Remove client from dictionary
            print(f"Removed client {client_address} from client list.")
        
        if client_socket:
            client_socket.close()
            print(f"Client socket closed for {client_address}")

    def close_server(self):
        for client_info in self.clients.values():
            client_info['socket'].close()  # Close each client socket
        self.clients.clear()  # Clear the client list
        if self.server_socket:
            self.server_socket.close()
            print("Server socket closed")

if __name__ == "__main__":
    server = MyServer()  
    server.start_server()
