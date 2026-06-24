from constants import *
from models import Snake, Food

class GameManager:
    def __init__(self):
        self.state = STATE_MENU
        self.snake = None
        self.food = None
        self.score = 0
        self.level = 1
        self.obstacles = []
        self.highscore = self.load_highscore()

    def load_highscore(self):
        try:
            lines = loadStrings("highscore.txt")
            if lines and len(lines) > 0:
                return int(lines[0])
        except Exception as e:
            println("Nie udało się wczytać najwyższego wyniku, ustawiam 0: " + str(e))
        return 0

    def save_highscore(self):
        try:
            saveStrings("data/highscore.txt", [str(self.highscore)])
        except Exception as e:
            println("Błąd zapisu rekordu: " + str(e))

    def start_new_game(self):
        self.snake = Snake()
        self.food = Food()
        self.score = 0
        self.level = 1
        self.load_level_layout()
        self.state = STATE_PLAYING
        frameRate(self.get_speed())

    def get_speed(self):
        return 8 + (self.level * 2)

    def load_level_layout(self):
        
        self.obstacles = []
        if self.level == 2:
            # Przeszkoda ~Ash
            for i in range(10, 20):
                self.obstacles.append(PVector(15, i))
        elif self.level == 3:
            # Przeszkoda next level ~Ash
            for i in range(5, 10):
                self.obstacles.append(PVector(5, i))
                self.obstacles.append(PVector(25, i))
                self.obstacles.append(PVector(5, ROWS - i))
                self.obstacles.append(PVector(25, ROWS - i))

    def update(self):
        if self.state != STATE_PLAYING:
            return

        self.snake.update()

        if self.snake.check_collision(self.obstacles):
            if self.score > self.highscore:
                self.highscore = self.score
                self.save_highscore()
            self.state = STATE_GAME_OVER

        head = self.snake.body[0]
        if head.x == self.food.pos.x and head.y == self.food.pos.y:
            self.snake.grow()
            self.food.pos = self.food.pick_location()
            self.score += 1
            
            # Nowy level co 5 punktów ~Ash
            new_level = (self.score // 5) + 1
            if new_level > self.level:
                self.level = new_level
                self.load_level_layout()
                frameRate(self.get_speed())
