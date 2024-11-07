import pygame, sys, random
from pygame.math import Vector2

class SNAKE:
    def __init__(self):
        # for the directions and for the body size and for the fruit size
        self.body = [Vector2(5,10),Vector2(4,10),Vector2(3,10)]
        self.direction = Vector2(1,0)
        self.new_block = False
        
        
        
    def draw_snake(self):
        for block in self.body:
            # position of the player and the visuals of the player
            x_pos = int(block.x * cell_size)
            y_pos = int(block.y * cell_size)
            snake_rect = pygame.Rect(x_pos, y_pos, cell_size, cell_size)
            pygame.draw.rect(screen, (100, 110, 152), snake_rect)

    def move_snake(self):
        if self.new_block:
            # adding a new block when you eat the fruit
            body_copy = self.body[:]
            body_copy.insert(0, body_copy[0] + self.direction)
            self.body = body_copy[:]
            self.new_block = False
        else:
            # for the movements of the body 
            body_copy = self.body[:-1]
            body_copy.insert(0, body_copy[0] + self.direction)
            self.body = body_copy[:]
    
    def add_block(self):
        # Setting the flag to True to indicate a new block should be added
        self.new_block = True

class FRUIT:
    # fruit location
    def __init__(self):
        self.randomize()
        
    # make the fruit visible on the screen and give it the size of the fruit 
    def draw_fruit(self):
        fruit_rect = pygame.Rect(int(self.pos.x * cell_size), int(self.pos.y * cell_size), cell_size, cell_size)
        screen.blit(cherry,fruit_rect)
        # pygame.draw.rect(screen, (126, 166, 114), fruit_rect)
    
    def randomize(self):
        self.x = random.randint(0, cell_number - 1)
        self.y = random.randint(0, cell_number - 1)
        self.pos = Vector2(self.x, self.y)

class MAIN:
    def __init__(self):
        self.snake = SNAKE()
        self.fruit = FRUIT()
        
    def update(self):
        self.snake.move_snake()
        self.check_collision()
        self.check_fail()  # Call check_fail here to end the game if the snake fails
        
    def draw_elements(self):
        self.fruit.draw_fruit()
        self.snake.draw_snake()
    
    def check_collision(self):
        if self.fruit.pos == self.snake.body[0]:
            self.fruit.randomize()
            self.snake.add_block()
    
    def check_fail(self):
        # Check if the snake hits the boundaries
        if not 0 <= self.snake.body[0].x < cell_number or not 0 <= self.snake.body[0].y < cell_number:
            self.game_over()
            
        # Check if the snake hits itself
        for block in self.snake.body[1:]:
            if block == self.snake.body[0]:
                self.game_over()
            
    def game_over(self):
        pygame.quit()
        sys.exit()

# basic size to start the game, the screen size, the name of the screen, and the fps clock
pygame.init()
cell_size = 35
cell_number = 20
screen = pygame.display.set_mode((cell_number * cell_size, cell_number * cell_size))
pygame.display.set_caption("Snake Window")
clock = pygame.time.Clock()
cherry = pygame.image.load('C:/Users/Ravag/Desktop/bit-academy/persoonlijke_projecten/python_games/python_snake/Graphics/cherry(1).png').convert_alpha()


# speed of the player 
SCREEN_UPDATE = pygame.USEREVENT
pygame.time.set_timer(SCREEN_UPDATE, 120)

main_game = MAIN()

while True:
    for event in pygame.event.get():
        # for the exit button
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == SCREEN_UPDATE:
            main_game.update()
        if event.type == pygame.KEYDOWN:
            # player inputs and directions action
            if event.key == pygame.K_w:
                if main_game.snake.direction.y != 1:
                    main_game.snake.direction = Vector2(0, -1)
            if event.key == pygame.K_s:
                if main_game.snake.direction.y != -1:
                    main_game.snake.direction = Vector2(0, 1)
            if event.key == pygame.K_a:
                if main_game.snake.direction.x != 1:
                    main_game.snake.direction = Vector2(-1, 0)
            if event.key == pygame.K_d:
                if main_game.snake.direction.x != -1:
                    main_game.snake.direction = Vector2(1, 0)

    # screen size, fps, loading of the fruit and the player
    screen.fill((130, 220, 75))
    main_game.draw_elements()
    pygame.display.update()
    clock.tick(60)
