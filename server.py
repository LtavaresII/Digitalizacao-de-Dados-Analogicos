import socket
import pickle
from painelqr import main, draw_buttons

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
        BUTTON_LAYOUT = [
            [array[0], array[3], array[6], array[9], array[12], array[15], array[18], array[21], array[24], array[27], array[30], array[33]],  # Primeira linha
            [array[1], array[4], array[7], array[10], array[13], array[16], array[19], array[22], array[25], array[28], array[31], array[34]],  # Segunda linha
            [array[2], array[5], array[8], array[11], array[14], array[17], array[20], array[23], array[26], array[29], array[32], array[35]],  # Terceira linha
            [array[36], array[38], array[40], 8, array[42]],  # Quarta linha
            [array[37], array[39], array[41], 8, array[43]]   # Quinta linha
        ]
        main(BUTTON_LAYOUT)
        #print(f"Array recebido: {array}")
except KeyboardInterrupt:
    print("\nEncerrando servidor...")
finally:
    # Fechar conexão
    conn.close()
    server_socket.close()