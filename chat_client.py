from Crypto.Cipher import AES
import socket
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

def start_client():
    clear_screen()
    server_ip = input("What Is IP of the server running: ")
    server_port = int(input("Enter Port No on which the server is running: "))
    client_username = input("Enter your username: ")

    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect((server_ip, server_port))
    
    print(f"Connected to the server at {server_ip}:{server_port}")

    while True:
        msg = input(colored(f"{client_username}-> ", "blue"))
        timestamped_msg = f"{get_current_time()} {client_username}: {msg}"
        if msg.lower() == 'bye':
            encrypted_msg = encrypt_message('bye'.encode('utf-8'))
            client.send(encrypted_msg)
            print(colored("You disconnected from the chat.", "red"))
            break
        encrypted_msg = encrypt_message(timestamped_msg.encode('utf-8'))
        client.send(encrypted_msg)

        try:
            encrypted_incoming_msg = client.recv(1024)
            if not encrypted_incoming_msg:
                print(colored("Server disconnected.", "red"))
                break
            incoming_msg = decrypt_message(encrypted_incoming_msg).decode('utf-8')
            if incoming_msg.lower() == 'bye':
                print(colored("Server disconnected from the chat.", "red"))
                break
            print(colored(incoming_msg, "green"))
        except ConnectionResetError:
            print(colored("Server disconnected unexpectedly.", "red"))
            break

    client.close()
    clear_screen()
    print("Disconnected from the server.")

if __name__ == "__main__":
    start_client()


