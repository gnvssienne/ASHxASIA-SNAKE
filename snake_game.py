from constants import *
from manager import GameManager


gm = GameManager()

def setup():
    size(600, 600)
    frameRate(10)

def draw():
    background(COLOR_BG)
    
    if gm.state == STATE_MENU:
        draw_menu()
    elif gm.state == STATE_PLAYING:
        gm.update()
        draw_gameplay()
    elif gm.state == STATE_GAME_OVER:
        draw_game_over()

def draw_menu():
    textAlign(CENTER)
    fill(255)
    textSize(36)
    text("SNAKE: ASH&ASIA", width / 2, height / 2 - 40)
    textSize(18)
    text("Najlepszy wynik (Highscore): " + str(gm.highscore), width / 2, height / 2)
    fill(50, 205, 50)
    text("Naciśnij SPACJĘ, aby rozpocząć", width / 2, height / 2 + 50)

def draw_gameplay():
    # Rysowanie jedzenia
    fill(COLOR_FOOD[0], COLOR_FOOD[1], COLOR_FOOD[2])
    rect(gm.food.pos.x * GRID_SIZE, gm.food.pos.y * GRID_SIZE, GRID_SIZE, GRID_SIZE)
    
    # Rysowanie węża
    fill(COLOR_SNAKE[0], COLOR_SNAKE[1], COLOR_SNAKE[2])
    for part in gm.snake.body:
        rect(part.x * GRID_SIZE, part.y * GRID_SIZE, GRID_SIZE, GRID_SIZE)
        
    # Rysowanie przeszkód 
    fill(COLOR_WALL[0], COLOR_WALL[1], COLOR_WALL[2])
    for obs in gm.obstacles:
        rect(obs.x * GRID_SIZE, obs.y * GRID_SIZE, GRID_SIZE, GRID_SIZE)

    # UI
    fill(255)
    textSize(16)
    textAlign(LEFT)
    text("Wynik: " + str(gm.score) + "  |  Poziom: " + str(gm.level), 15, 30)

def draw_game_over():
    textAlign(CENTER)
    fill(255, 50, 50)
    textSize(42)
    text("KONIEC GRY", width / 2, height / 2 - 20)
    fill(255)
    textSize(20)
    text("Twój wynik: " + str(gm.score), width / 2, height / 2 + 20)
    text("Naciśnij 'R', aby powrócić do menu", width / 2, height / 2 + 60)

def keyPressed():
    if gm.state == STATE_MENU:
        if key == ' ':
            gm.start_new_game()
            
    elif gm.state == STATE_PLAYING:
        if keyCode == UP:
            gm.snake.set_dir(0, -1)
        elif keyCode == DOWN:
            gm.snake.set_dir(0, 1)
        elif keyCode == LEFT:
            gm.snake.set_dir(-1, 0)
        elif keyCode == RIGHT:
            gm.snake.set_dir(1, 0)
            
    elif gm.state == STATE_GAME_OVER:
        if key == 'r' or key == 'R':
            gm.state = STATE_MENU
            frameRate(10) # Przywrócenie płynności menu