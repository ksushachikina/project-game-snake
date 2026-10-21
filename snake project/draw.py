import pygame

CELL_NUMBER = 20
CELL_SIZE = 40

WINDOW = CELL_NUMBER * CELL_SIZE
BUTTON = pygame.Rect(WINDOW // 2 - 150, 350, 300, 50)

class Draw:
    def __init__(self, screen: pygame.Surface) -> None:
        self.screen = screen
        self.font_for_score = pygame.font.SysFont("arial", 25, bold=True)
        self.big_font = pygame.font.SysFont("arial", 70, bold=True)
        self.font = pygame.font.SysFont("arial", 40, bold=True)

    def game_board(self):
        self.screen.fill((199, 252, 205))
        for row in range(CELL_NUMBER):
            for col in range(CELL_NUMBER):
                if (row + col) % 2 == 0:
                    x = col * CELL_SIZE
                    y = row * CELL_SIZE
                    pygame.draw.rect(self.screen, (139,232,153), (x, y, CELL_SIZE, CELL_SIZE))

    def score(self, current_score, score):
        place = pygame.Surface((WINDOW, 44), pygame.SRCALPHA)
        place.fill((165,220,172,150))
        self.screen.blit(place, (0,0))
        text = self.font_for_score.render(f"Счёт: {current_score}", True, (10, 79, 168))
        self.screen.blit(text, (10, 10))

        record = self.font_for_score.render(f"Рекорд: {score}", True, (10, 79, 168))
        self.screen.blit(record, record.get_rect(topright=(WINDOW - 10, 10)))

    def text_center(self, text, font, color, y):
        message = font.render(text, True, color)
        self.screen.blit(message, message.get_rect(center=(WINDOW // 2, y)))

    def start_screen(self):
        self.screen.fill((199,252,205))
        self.text_center("Snake Game", self.big_font, (10, 79, 168), 250)
        self.buttons("Играть")

    def game_over_screen(self, current_score, score):
        message = pygame.Surface((WINDOW, WINDOW), pygame.SRCALPHA)
        message.fill((60,70,100,200))
        self.screen.blit(message, (0,0))
        self.text_center("Game Over", self.big_font, (255,255,255), 200)
        self.text_center(f"Счет: {current_score}    Рекорд: {score}", self.font, (10, 79, 168), 290)
        self.buttons("Играть")

    def buttons(self, name):
        pygame.draw.rect(self.screen, (10, 79, 168), BUTTON, border_radius=26)
        text = self.font.render(name, True, (255,255,255))
        self.screen.blit(text, text.get_rect(center=BUTTON.center))