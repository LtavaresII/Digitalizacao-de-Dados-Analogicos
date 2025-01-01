import socket
import pickle
from painelqr import main, buttons_layout
# Configurações do servidor
HOST = '127.0.0.1'  # Endereço IP do servidor (localhost)
PORT = 65432        # Porta para escutar conexões
# Criação do socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((HOST, PORT))
server_socket.listen()
print("Servidor aguardando conexão...")
# Aceitar conexões
conn, addr = server_socket.accept()
print(f"Conectado por {addr}")
# Loop para receber continuamente
try:
    while True:
        data = conn.recv(1024)  # Tamanho do buffer
        if not data:  # Se não houver dados, encerra o loop
            break
        array = pickle.loads(data)  # Desserializar o array
        BUTTON_LAYOUT = buttons_layout(array)
        main(BUTTON_LAYOUT)
except KeyboardInterrupt:
    print("\nEncerrando servidor...")
finally:
    # Fechar conexão
    conn.close()
    server_socket.close()