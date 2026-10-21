import pygame
import sys
import random
from draw import CELL_SIZE

def load_image(path):
    try:
        image = pygame.image.load(path).convert_alpha()
    except (pygame.error, FileNotFoundError):
        print(f"Не удалось загрузить картинку: {path}")
        pygame.quit()
        sys.exit(1)
    return pygame.transform.scale(image, (CELL_SIZE, CELL_SIZE))


class Apple:
    def __init__(self, cell_number):
        self.cell_number = cell_number
        self.place = (0, 0)
        self.apple_image = load_image("images/apple.png")

    def draw_apple(self, screen):
        apple = pygame.Rect(
            int(self.place[0] * CELL_SIZE),
            int(self.place[1] * CELL_SIZE),
            CELL_SIZE,
            CELL_SIZE,
        )
        screen.blit(self.apple_image, apple)

    def new_place(self, snake_body):
        while True:
            x = random.randint(0, self.cell_number - 1)
            y = random.randint(0, self.cell_number - 1)
            if (x, y) not in snake_body:
                self.place = (x, y)
                break


class Snake:
    def __init__(self):
        self.body = [(6, 10), (5, 10)]
        self.move_to = (1, 0)
        self.queue = []

        self.head_right = load_image("images/head_right.png")
        self.head_left = load_image("images/head_left.png")
        self.head_up = load_image("images/head_up.png")
        self.head_down = load_image("images/head_down.png")

        self.tail_right = load_image("images/tail_right.png")
        self.tail_left = load_image("images/tail_left.png")
        self.tail_up = load_image("images/tail_up.png")
        self.tail_down = load_image("images/tail_down.png")

        self.body_right = load_image("images/body_right.png")
        self.body_up = load_image("images/body_up.png")

        self.body_down_right = load_image("images/body_down_right.png")
        self.body_up_right = load_image("images/body_up_right.png")
        self.body_down_left = load_image("images/body_down_left.png")
        self.body_up_left = load_image("images/body_up_left.png")

    def turn(self, direction):
        last = self.queue[-1] if self.queue else self.move_to
        if direction == last or direction == (-last[0], -last[1]):
            return
        if len(self.queue) < 2:
            self.queue.append(direction)

    def next_head(self):
        direction = self.queue[0] if self.queue else self.move_to
        return (self.body[0][0] + direction[0], self.body[0][1] + direction[1])

    def move_snake(self, grow=False):
        if self.queue:
            self.move_to = self.queue.pop(0)
        new_head = (self.body[0][0] + self.move_to[0], self.body[0][1] + self.move_to[1])
        if grow:
            self.body = [new_head] + self.body
        else:
            self.body = [new_head] + self.body[:-1]

    def draw_snake(self, screen):
        for number, part in enumerate(self.body):
            x, y = part
            part_snake = pygame.Rect(x * CELL_SIZE, y * CELL_SIZE, CELL_SIZE, CELL_SIZE)

            if number == 0:
                position = (x - self.body[1][0], y - self.body[1][1])
                images = {
                    (1, 0): self.head_right, (0, 1): self.head_down,
                    (0, -1): self.head_up, (-1, 0): self.head_left,
                }
                screen.blit(images[position], part_snake)

            elif number == len(self.body) - 1:
                position = (x - self.body[number - 1][0], y - self.body[number - 1][1])
                images = {
                    (1, 0): self.tail_right, (0, 1): self.tail_down,
                    (0, -1): self.tail_up, (-1, 0): self.tail_left,
                }
                screen.blit(images[position], part_snake)

            elif self.body[number + 1][0] == self.body[number - 1][0]:
                screen.blit(self.body_up, part_snake)

            elif self.body[number + 1][1] == self.body[number - 1][1]:
                screen.blit(self.body_right, part_snake)

            else:
                nxt = self.body[number + 1]
                prev = self.body[number - 1]
                sides = {(nxt[0] - x, nxt[1] - y), (prev[0] - x, prev[1] - y)}
                if sides == {(1, 0), (0, -1)}:
                    screen.blit(self.body_down_right, part_snake)
                elif sides == {(1, 0), (0, 1)}:
                    screen.blit(self.body_up_right, part_snake)
                elif sides == {(-1, 0), (0, 1)}:
                    screen.blit(self.body_up_left, part_snake)
                elif sides == {(-1, 0), (0, -1)}:
                    screen.blit(self.body_down_left, part_snake)