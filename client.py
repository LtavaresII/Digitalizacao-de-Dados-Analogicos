import socket
import pickle
import time
import cv2
from qrreader import read_qr_codes, centralize_image, get_brightness
# Configurações do cliente
HOST = '127.0.0.1'  # Endereço IP do servidor
PORT = 65432        # Porta para conexão
# Array base para enviar
array_to_send = [1, 2, 3, 4, 5]
# Criação do socket
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((HOST, PORT))
try:
    while True:
        # Atualizando o array
        #cap = cv2.VideoCapture(1)
        #frame = get_frame(cap)
        frame = cv2.imread("PainelQR.jpg")
        if frame is None:
            raise FileNotFoundError("Não foi possível carregar a imagem.")
        frame = cv2.resize(frame, (1280, 720))
        positions = read_qr_codes(frame)
        frame_centered = centralize_image(frame, positions)
        _, on_off = get_brightness(frame_centered)
        array_to_send = on_off
        # Serializar o array
        data = pickle.dumps(array_to_send)
        # Enviar dados
        client_socket.sendall(data)
        # Aguardar antes de enviar novamente
        time.sleep(1)  # Envia a cada 1 segundos
except KeyboardInterrupt:
    print("\nEncerrando cliente...")
finally:
    # Fechar conexão
    client_socket.close()