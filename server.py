import socket
import json

def read_data(file_path):
    try:
        with open(file_path, 'r') as file:
            data = json.load(file)
        return data
    except FileNotFoundError:
        return {}

def write_data(file_path, data):
    with open(file_path, 'w') as file:
        json.dump(data, file)
        file.write('\n')

def handle_command(command, data, client_socket):
    action, attribute, person_name = command.split(" ", 2)

    if action == "Read":
        response = data.get(person_name, {}).get(attribute, "Attribute not found.")
        client_socket.send(response.encode())

    elif action == "Write":
        if person_name not in data:
            data[person_name] = {}
        data[person_name][attribute] = input(f"Enter value for {attribute}: ")
        write_data(FILE_PATH, data +'\n')
        client_socket.send("Write successful.".encode())

    else:
        client_socket.send("Invalid command.".encode())

def start_server():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((HOST, PORT))
    server_socket.listen()

    print(f"Server listening on {HOST}:{PORT}")

    while True:
        client_socket, address = server_socket.accept()
        print(f"Connection from {address}")

        data = read_data(FILE_PATH)

        command = client_socket.recv(BUFFER_SIZE).decode()
        handle_command(command, data, client_socket)

        client_socket.close()

if __name__ == "__main__":
    HOST = '127.0.0.1'
    PORT = 12345
    BUFFER_SIZE = 1024
    FILE_PATH = 'data.json'

    start_server()
