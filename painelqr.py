import pygame
import sys

# Configurações iniciais
SCREEN_WIDTH, SCREEN_HEIGHT = 1280, 768
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
    [3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3],  # Quarta linha
    [4, 4, 4, 8, 4],  # Quinta linha
    [5, 5, 5, 8, 5],  # Sexta linha
    [3, 3, 3, 8, 8]   # Setima linha
]

# Array com a informação do que cada botão significa 

NAMES = ["CHEFE MISSÃO", "C. AVANÇADO", "SEG. VOO", "SEG. SUPERFICIE", "ADOUR", "BEARN", "TELEMEDIDAS", 
         "SVO.02", "LOGISTICA", "TRAJ.", "VISU SINTESE", "EMI C/IMPASSE", "TELEMEDIDAS", "BEARN", "ADOUR","",""]

# Inicializa o pygame
#pygame.init()
#screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
#pygame.display.set_caption("Painel de Luzes")
#clock = pygame.time.Clock()

def draw_buttons(screen, layout, names):
    """Desenha os botões com base no layout."""
    y_start = 75 # Início da primeira linha no eixo Y
    x_start = 75  # Início no eixo X
    i=0
    for row_idx, row in enumerate(layout):
        for col_idx, state in enumerate(row):
            if row_idx == 2 or (col_idx == 11 and row_idx !=3):
                x = x_start + col_idx * (BUTTON_SPACING + 50) + 25
                y = y_start + row_idx * (BUTTON_SPACING + 50) + 25
                pygame.draw.circle(screen, BUTTON_COLORS[state], (x, y), 25)
                pygame.draw.circle(screen, (0,0,0), (x, y), 25, 2)
            elif (row_idx == 4 and col_idx == 3) or (row_idx == 5 and col_idx == 3) or (row_idx == 6 and col_idx == 3) or (row_idx == 6 and col_idx == 4):
                x = x_start + col_idx * (BUTTON_SIZE + BUTTON_SPACING)
                y = y_start + row_idx * (BUTTON_SIZE + BUTTON_SPACING)
                pygame.draw.rect(screen, BUTTON_COLORS[state], (x, y, BUTTON_SIZE, BUTTON_SPACING))
            elif (row_idx == 3 or row_idx == 6):
                x = (x_start-25) + col_idx * (BUTTON_SIZE + BUTTON_SPACING)
                y = y_start + row_idx * (BUTTON_SIZE + BUTTON_SPACING)
                rect=pygame.draw.rect(screen, BUTTON_COLORS[state], (x, y, BUTTON_SIZE*2, BUTTON_SPACING))
                pygame.draw.rect(screen, (0,0,0), (x, y, BUTTON_SIZE*2, BUTTON_SPACING), 2)
                font = pygame.font.Font(None, 15)
                text_surface = font.render(names[i], True, (0,0,0))
                text_rect = text_surface.get_rect(center=rect.center)
                screen.blit(text_surface, text_rect)
                i+=1
            else:
                x = x_start + col_idx * (BUTTON_SIZE + BUTTON_SPACING)
                y = y_start + row_idx * (BUTTON_SIZE + BUTTON_SPACING)
                pygame.draw.rect(screen, BUTTON_COLORS[state], (x, y, BUTTON_SIZE, BUTTON_SPACING))
                pygame.draw.rect(screen, (0,0,0), (x, y, BUTTON_SIZE, BUTTON_SPACING), 2)


def main(BUTTON_LAYOUT, NAMES):
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
        
        draw_buttons(screen, BUTTON_LAYOUT, NAMES)
        pygame.display.flip()
        clock.tick(60)

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main(BUTTON_LAYOUT, NAMES)