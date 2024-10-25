# Multi-Client Chat Server


This project is a Multi-Client Chat Server implemented in Python, which supports concurrent connections from multiple clients using threading. The server listens for client connections on a specified port and provides real-time message handling with simple echo functionality, responding to each client's messages in uppercase. The project demonstrates basic socket programming, multi-threading, and client management using Python.

# Features

Multi-Client Support: Allows multiple clients to connect to the server simultaneously, with each client handled in a separate thread.

Real-Time Communication: Each connected client can send messages at any time and receive real-time responses from the server.

Client Management: The server keeps track of all connected clients using a dictionary, making it easy to manage and track each client’s connection.

Graceful Disconnection: Clients can close their connection by sending a specific command ("CLOSE SOCKET"), and the server will remove them from its records and close the connection.

Echo Response: The server echoes each message sent by a client in uppercase.
