import socket
import pickle
from painelqr import buttons_layout, draw_buttons, NAMES,SCREEN_WIDTH,SCREEN_HEIGHT
import pygame
import sys
# Configurações do servidor
HOST = '127.0.0.1'  # Endereço IP do servidor (localhost)
PORT = 65432        # Porta para escutar conexões
#
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
    # Inicializa o pygame
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("Painel de Luzes")
    clock = pygame.time.Clock()
    running = True
    while running:
        data = conn.recv(1024)  # Tamanho do buffer
        if not data:  # Se não houver dados, encerra o loop
            break
        array = pickle.loads(data)  # Desserializar o array
        BUTTON_LAYOUT = buttons_layout(array)
        
        screen.fill((100, 100, 100))  # Cor de fundo
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        
        draw_buttons(screen, BUTTON_LAYOUT, NAMES)
        pygame.display.flip()
        clock.tick(60)
except KeyboardInterrupt:
    print("\nEncerrando servidor...")
finally:
    # Fechar conexão
    pygame.quit()
    sys.exit()
    conn.close()
    server_socket.close()