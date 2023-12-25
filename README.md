# P2P Chat with AES Encryption

## Project Overview
This project is a secure communication platform that enables users to engage in encrypted chat through a terminal interface. Utilizing a peer-to-peer (P2P) architecture, it enhances privacy and eliminates the need for centralized servers. Developed in Python, the application includes two scripts, `chat_server.py` and `chat_client.py`, to facilitate server and client roles, respectively. AES encryption is employed to secure the messages, ensuring confidentiality and integrity.

## System Requirements
- Compatible with Windows, Linux, macOS.
- Python 3.

## Setup Instructions

### Installing Python and Pip
1. Verify if Python 3 is installed: `python3 --version`.
2. If Python 3 is not installed, download and install it from the official Python website.
3. Ensure pip (Python package manager) is installed.

### Installing Required Python Libraries
1. Install `termcolor` for colored terminal output: `pip3 install termcolor`.
2. Install `pycryptodome` for AES encryption: `pip3 install pycryptodome`.

### Downloading the Project Scripts
1. Obtain `chat_server.py` and `chat_client.py` scripts for server and client functionalities.

### Running the Chat Server
1. Open a terminal (or command prompt in Windows) and navigate to the directory containing `chat_server.py`.
2. Start the server: `python3 chat_server.py`.

### Running the Chat Client
1. Open a new terminal (or command prompt in Windows) on the client machine and navigate to where `chat_client.py` is located.
2. Start the client: `python3 chat_client.py`.
3. When prompted, enter the server's IP address to establish a connection.

### Initiating Secure Chat
- Once connected, the server and client can communicate securely with AES-encrypted messages.

### Ending the Chat Session
- To end the chat session, type 'bye' in either the server or client terminal.

## Security Note
- Ensure the AES encryption key is securely shared between the server and client before initiating the chat.
