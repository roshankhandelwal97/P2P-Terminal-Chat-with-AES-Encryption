from Crypto.Cipher import AES 
import socket
import threading
import os
import datetime
from termcolor import colored

banner = '''
    ____ _   _    _  _____ 
   / ___| | | |  / \|_   _|
  | |   | |_| | / _ \ | |  
  | |___|  _  |/ ___ \| |  
   \____|_| |_/_/   \_\_|  
                                                                               
'''
print(banner)

# AES Encryption Setup
key = b'16bytekey1234567'  # 16 bytes key
iv = b'16byteiv12345678'   # 16 bytes IV

def encrypt_message(message):
    cipher = AES.new(key, AES.MODE_CFB, iv)
    return cipher.encrypt(message)

def decrypt_message(encrypted_message):
    cipher = AES.new(key, AES.MODE_CFB, iv)
    return cipher.decrypt(encrypted_message)

def clear_screen():
    if os.name == 'nt':  # Windows
        os.system('cls')
    else:  # macOS and Linux
        os.system('clear')

def get_current_time():
    return datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

def handle_client(client_socket):
    while True:
        encrypted_msg = client_socket.recv(1024)
        msg = decrypt_message(encrypted_msg).decode('utf-8')
        if msg == 'bye':
            break
        if msg:
            print(f"Client: {msg}")

    client_socket.close()
    clear_screen()
    print("Connection closed.")
    os._exit(0)

def start_server():
    clear_screen()
    server_ip = input("Enter The Local IP of your Machine: ")
    server_port = int(input("Enter The port no. to bind: "))
    server_username = input("Enter your username: ")

    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((server_ip, server_port))
    server.listen(1)

    print(f"Server listening on {server_ip}:{server_port}")

    client_socket, addr = server.accept()
    print(f"[+] {addr} Connected")

    client_thread = threading.Thread(target=handle_client, args=(client_socket,))
    client_thread.start()

    while True:
        msg = input(colored(f"{server_username}-> ", "blue"))
        timestamped_msg = f"{get_current_time()} {server_username}: {msg}"
        if msg.lower() == 'bye':
            encrypted_msg = encrypt_message('bye'.encode('utf-8'))
            client_socket.send(encrypted_msg)
            print(colored("You disconnected from the chat.", "red"))
            break
        encrypted_msg = encrypt_message(timestamped_msg.encode('utf-8'))
        client_socket.send(encrypted_msg)

    client_socket.close()
    server.close()

if __name__ == "__main__":
    start_server()

