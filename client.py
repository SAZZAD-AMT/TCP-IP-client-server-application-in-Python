import socket

def send_command(command):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client_socket:
        client_socket.connect((SERVER_HOST, SERVER_PORT))
        client_socket.send(command.encode())
        response = client_socket.recv(BUFFER_SIZE).decode()
        print(f"Server response: {response}")

if __name__ == "__main__":
    SERVER_HOST = '127.0.0.1'
    SERVER_PORT = 12345
    BUFFER_SIZE = 1024

    while True:
        command = input("Enter command (e.g., Read/Write \"Attribute\" \"Person Name\"): ")
        send_command(command)
