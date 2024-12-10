import pygame
import sys

# Configurações iniciais
SCREEN_WIDTH, SCREEN_HEIGHT = 1280, 720
BUTTON_SIZE = 50  # Tamanho dos botões
BUTTON_SPACING = 50  # Espaço entre botões
BUTTON_ROWS = 5
BUTTON_COLORS = {
    # Acesso
    0: (255, 0, 0),  # Vermelho
    1: (0, 255, 0),  # Verde
    2: (0, 0, 255),  # Azul
    3: (255, 255, 255),  # Branco
    # Apagado
    4: (125, 0, 0),  # Vermelho
    5: (0, 127, 0),  # Verde
    6: (0, 0, 127),  # Azul
    7: (127, 127, 127),  # Branco
    # Vazio
    8: (100, 100, 100) 
}

# Posições e estados iniciais das luzes
BUTTON_LAYOUT = [
    [4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4],  # Primeira linha
    [5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5],  # Segunda linha
    [6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 7, 7],  # Terceira linha
    [4, 4, 4, 8, 4],  # Quarta linha
    [5, 5, 5, 8, 5]   # Quinta linha
]

# Inicializa o pygame
#pygame.init()
#screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
#pygame.display.set_caption("Painel de Luzes")
#clock = pygame.time.Clock()

def draw_buttons(screen, layout):
    """Desenha os botões com base no layout."""
    y_start = 150  # Início da primeira linha no eixo Y
    x_start = 75  # Início no eixo X
    for row_idx, row in enumerate(layout):
        for col_idx, state in enumerate(row):
            if row_idx == 2:
                x = x_start + col_idx * (BUTTON_SPACING + 50) + 25
                y = y_start + row_idx * (BUTTON_SPACING + 50) + 25
                pygame.draw.circle(screen, BUTTON_COLORS[state], (x, y), 25)
                pygame.draw.circle(screen, (0,0,0), (x, y), 25, 2)
            elif (row_idx == 3 and col_idx == 3) or (row_idx == 4 and col_idx == 3):
                x = x_start + col_idx * (BUTTON_SIZE + BUTTON_SPACING)
                y = y_start + row_idx * (BUTTON_SIZE + BUTTON_SPACING)
                pygame.draw.rect(screen, BUTTON_COLORS[state], (x, y, BUTTON_SIZE, BUTTON_SPACING))
            else:
                x = x_start + col_idx * (BUTTON_SIZE + BUTTON_SPACING)
                y = y_start + row_idx * (BUTTON_SIZE + BUTTON_SPACING)
                pygame.draw.rect(screen, BUTTON_COLORS[state], (x, y, BUTTON_SIZE, BUTTON_SPACING))
                pygame.draw.rect(screen, (0,0,0), (x, y, BUTTON_SIZE, BUTTON_SPACING), 2)

def main(BUTTON_LAYOUT):
    # Inicializa o pygame
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("Painel de Luzes")
    clock = pygame.time.Clock()

    running = True
    while running:
        screen.fill((100, 100, 100))  # Cor de fundo
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        
        draw_buttons(screen, BUTTON_LAYOUT)
        pygame.display.flip()
        clock.tick(60)

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main(screen,BUTTON_LAYOUT)