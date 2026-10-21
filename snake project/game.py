from objects import Snake, Apple
from score import find_score, save_score

POINTS = 1

class Game:
    def __init__(self, cell_number, cell_size):
        self.cell_number = cell_number
        self.cell_size = cell_size

        self.snake = Snake()
        self.apple = Apple(cell_number)

        self.apple.new_place(self.snake.body)
        self.current_score = 0
        self.score = find_score()
        self.game_over = False

    def update(self):
        grow = self.snake.next_head() == self.apple.place
        self.snake.move_snake(grow)
        if grow:
            self.current_score += POINTS
            self.score = max(self.score, self.current_score)
            self.apple.new_place(self.snake.body)
        self.end_of_game()

    def draw(self, screen):
        self.apple.draw_apple(screen)
        self.snake.draw_snake(screen)

    def end_of_game(self):
        head = self.snake.body[0]
        out = not (0 <= head[0] < self.cell_number and 0 <= head[1] < self.cell_number)
        if out or head in self.snake.body[1:]:
            save_score(self.score)
            self.game_over = True