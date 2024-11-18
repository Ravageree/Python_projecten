import pygame, sys, random
from pygame.math import Vector2

highscore = 0

class SNAKE:
    def __init__(self):
        # for the directions and for the body size and for the fruit size
        self.body = [Vector2(5,10),Vector2(4,10),Vector2(3,10)]
        self.direction = Vector2(1,0)
        self.new_block = False
        
        self.head_up = pygame.image.load('C:/Users/Ravag/Desktop/bit-academy/persoonlijke_projecten/python_games/python_snake/Graphics/head_up.png').convert_alpha()
        self.head_down = pygame.image.load('C:/Users/Ravag/Desktop/bit-academy/persoonlijke_projecten/python_games/python_snake/Graphics/head_down.png').convert_alpha()
        self.head_left = pygame.image.load('C:/Users/Ravag/Desktop/bit-academy/persoonlijke_projecten/python_games/python_snake/Graphics/head_left.png').convert_alpha()
        self.head_right = pygame.image.load('C:/Users/Ravag/Desktop/bit-academy/persoonlijke_projecten/python_games/python_snake/Graphics/head_right.png').convert_alpha()
        
        self.tail_up = pygame.image.load('C:/Users/Ravag/Desktop/bit-academy/persoonlijke_projecten/python_games/python_snake/Graphics/tail_up.png').convert_alpha()
        self.tail_down = pygame.image.load('C:/Users/Ravag/Desktop/bit-academy/persoonlijke_projecten/python_games/python_snake/Graphics/tail_down.png').convert_alpha()
        self.tail_left = pygame.image.load('C:/Users/Ravag/Desktop/bit-academy/persoonlijke_projecten/python_games/python_snake/Graphics/tail_left.png').convert_alpha()
        self.tail_right = pygame.image.load('C:/Users/Ravag/Desktop/bit-academy/persoonlijke_projecten/python_games/python_snake/Graphics/tail_right.png').convert_alpha()
        
        self.body_vertical = pygame.image.load('C:/Users/Ravag/Desktop/bit-academy/persoonlijke_projecten/python_games/python_snake/Graphics/body_vertical.png').convert_alpha()
        self.body_horizontal = pygame.image.load('C:/Users/Ravag/Desktop/bit-academy/persoonlijke_projecten/python_games/python_snake/Graphics/body_horizontal.png').convert_alpha()
        
        self.body_tr = pygame.image.load('C:/Users/Ravag/Desktop/bit-academy/persoonlijke_projecten/python_games/python_snake/Graphics/body_tr.png').convert_alpha()
        self.body_tl = pygame.image.load('C:/Users/Ravag/Desktop/bit-academy/persoonlijke_projecten/python_games/python_snake/Graphics/body_tl.png').convert_alpha()
        self.body_br = pygame.image.load('C:/Users/Ravag/Desktop/bit-academy/persoonlijke_projecten/python_games/python_snake/Graphics/body_br.png').convert_alpha()
        self.body_bl = pygame.image.load('C:/Users/Ravag/Desktop/bit-academy/persoonlijke_projecten/python_games/python_snake/Graphics/body_bl.png').convert_alpha() 
        self.fruit_sound = pygame.mixer.Sound('C:/Users/Ravag/Desktop/bit-academy/persoonlijke_projecten/python_games/python_snake/sounds/ding-sound-246413.mp3')
         
    def draw_snake(self):
        self.update_head_graphics()
        self.update_tail_graphics()
        
        for index,block in enumerate(self.body):
            x_pos = int(block.x * cell_size)
            y_pos = int(block.y * cell_size)
            block_rect = pygame.Rect(x_pos,y_pos,cell_size,cell_size)
            
            # the direction that the player is facing and update the visiules
            if index == 0:
                screen.blit(self.head,block_rect)
            elif index == len(self.body) - 1:
                screen.blit(self.tail,block_rect)
            else:
                previous_block = self.body[index + 1] - block
                next_block = self.body[index - 1] - block
                if previous_block.x == next_block.x:
                    screen.blit(self.body_vertical,block_rect)
                elif previous_block.y == next_block.y:
                    screen.blit(self.body_horizontal,block_rect)
                else:
                    if previous_block.x == -1 and next_block.y == -1 or previous_block.y == -1 and next_block.x == -1:
                        screen.blit(self.body_tl,block_rect)
                    elif previous_block.x == -1 and next_block.y == 1 or previous_block.y == 1 and next_block.x == -1:
                        screen.blit(self.body_bl,block_rect)
                    elif previous_block.x == 1 and next_block.y == -1 or previous_block.y == -1 and next_block.x == 1:
                        screen.blit(self.body_tr,block_rect)
                    elif previous_block.x == 1 and next_block.y == 1 or previous_block.y == 1 and next_block.x == 1:
                        screen.blit(self.body_br,block_rect)
                
    def update_head_graphics(self):
        head_direction = self.body[1] - self.body[0]
        
        if head_direction == Vector2(1,0):
            self.head = self.head_left
        elif head_direction == Vector2(-1,0):
            self.head = self.head_right
        elif head_direction == Vector2(0,1):
            self.head = self.head_up
        elif head_direction == Vector2(0,-1):
            self.head = self.head_down

    def update_tail_graphics(self):
        tail_direction = self.body[-2] - self.body[-1]
        
        if tail_direction == Vector2(1,0):
            self.tail = self.tail_left
        elif tail_direction == Vector2(-1,0):
            self.tail = self.tail_right
        elif tail_direction == Vector2(0,1):
            self.tail = self.tail_up
        elif tail_direction == Vector2(0,-1):
            self.tail = self.tail_down
            
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

    def play_fruit_sound(self):
        self.fruit_sound.play()

    def reset(self):
        self.body = [Vector2(5,10),Vector2(4,10),Vector2(3,10)]
        self.direction = Vector2(1,0)
        
        
class FRUIT:
    # fruit location
    def __init__(self):
        self.randomize()
        
    # make the fruit visible on the screen and give it the size of the fruit 
    def draw_fruit(self):
        fruit_rect = pygame.Rect(int(self.pos.x * cell_size), int(self.pos.y * cell_size), cell_size, cell_size)
        screen.blit(cherry,fruit_rect)
    
    def randomize(self):
        self.x = random.randint(0, cell_number - 1)
        self.y = random.randint(0, cell_number - 1)
        self.pos = Vector2(self.x, self.y)

class MAIN:
    def __init__(self):
        self.snake = SNAKE()
        self.fruit = FRUIT()
        self.game_over_sound = pygame.mixer.Sound('C:/Users/Ravag/Desktop/bit-academy/persoonlijke_projecten/python_games/python_snake/sounds/game-over-160612.mp3')
        self.is_game_over = False

    def update(self):
        if not self.is_game_over:
            self.snake.move_snake()
            self.check_collision()
            self.check_fail()

    def draw_elements(self):
        if not self.is_game_over:
            self.draw_grass()
            self.fruit.draw_fruit()
            self.snake.draw_snake()
            self.draw_score()
        else:
            self.draw_game_over()

    def check_collision(self):
        if self.fruit.pos == self.snake.body[0]:
            self.fruit.randomize()
            self.snake.add_block()
            self.snake.play_fruit_sound()
        
        # Ensure fruit does not spawn on the snake's body
        for block in self.snake.body[1:]:
            if block == self.fruit.pos:
                self.fruit.randomize()
    
    def check_fail(self):
        if not 0 <= self.snake.body[0].x < cell_number or not 0 <= self.snake.body[0].y < cell_number:
            self.game_over()
        for block in self.snake.body[1:]:
            if block == self.snake.body[0]:
                self.game_over()
    
    def draw_grass(self):
        grass_color = (125,209,70)
        for row in range(cell_number):
            if row % 2 == 0:
                for col in range(cell_number):
                    if col % 2 == 0:
                        grass_rect = pygame.Rect(col * cell_size,row * cell_size,cell_size,cell_size)
                        pygame.draw.rect(screen,grass_color,grass_rect)
            else:
                for col in range(cell_number):
                    if col % 2 != 0:
                        grass_rect = pygame.Rect(col * cell_size,row * cell_size,cell_size,cell_size)
                        pygame.draw.rect(screen,grass_color,grass_rect)

    def game_over(self):
        global highscore
        self.is_game_over = True
        game_sound.set_volume(0.0)
        self.game_over_sound.play()
        score = len(self.snake.body) - 3
        if score > highscore:
            highscore = score

    def draw_game_over(self):
        game_over_text = game_font.render("GAME OVER", True, (255, 0, 0))
        score_text = game_font.render(f"Score: {len(self.snake.body) - 3}", True, (255, 255, 255))
        highscore_text = game_font.render(f"Highscore: {highscore}", True, (255, 255, 255))
        restart_text = game_font.render("Press R to Restart or Q to Quit", True, (255, 255, 255))

        screen.fill((0, 0, 0))
        screen.blit(game_over_text, (screen.get_width() // 2 - game_over_text.get_width() // 2, screen.get_height() // 4))
        screen.blit(score_text, (screen.get_width() // 2 - score_text.get_width() // 2, screen.get_height() // 4 + 50))
        screen.blit(highscore_text, (screen.get_width() // 2 - highscore_text.get_width() // 2, screen.get_height() // 4 + 100))
        screen.blit(restart_text, (screen.get_width() // 2 - restart_text.get_width() // 2, screen.get_height() // 4 + 150))

    def reset(self):
        self.snake.reset()
        game_sound.set_volume(0.2)
        self.is_game_over = False
        pygame.time.set_timer(SCREEN_UPDATE, 150)

    def draw_score(self):
        score_text = str(len(self.snake.body) - 3)
        score_surface = game_font.render(score_text, True, (56, 74, 12))
        score_x = int(cell_size * cell_number) - 60
        score_y = int(cell_size * cell_number) - 40
        score_rect = score_surface.get_rect(center=(score_x, score_y))
        cherry_rect = cherry.get_rect(midright=(score_rect.left, score_rect.centery))
        
        screen.blit(score_surface, score_rect)
        screen.blit(cherry, cherry_rect)
     
# basic size to start the game, the screen size, the name of the screen, and the fps clock
pygame.mixer.pre_init(44100,-16,2,512)
pygame.init()
cell_size = 35
cell_number = 20
screen = pygame.display.set_mode((cell_number * cell_size, cell_number * cell_size))
pygame.display.set_caption("Snake Window")
clock = pygame.time.Clock()
game_sound = pygame.mixer.Sound('C:/Users/Ravag/Desktop/bit-academy/persoonlijke_projecten/python_games/python_snake/sounds/flat-8-bit-gaming-music-instrumental-211547.mp3')
game_sound.play(-1)
game_sound.set_volume(0.2)
cherry = pygame.image.load('C:/Users/Ravag/Desktop/bit-academy/persoonlijke_projecten/python_games/python_snake/Graphics/cherry(1).png').convert_alpha()
game_font = pygame.font.Font('C:/Users/Ravag/Desktop/bit-academy/persoonlijke_projecten/python_games/python_snake/font/BLAUSERUM.ttf',25)

 
main_game = MAIN()
# Adjust snake speed based on score
score = len(main_game.snake.body) - 3  # start length is 3
SCREEN_UPDATE = pygame.USEREVENT
if score > 10:
    interval = max(50, 150 - (score - 10) * 10)  # Decrease interval for higher speeds
    pygame.time.set_timer(SCREEN_UPDATE, interval)
else:
    pygame.time.set_timer(SCREEN_UPDATE, 150)  # Base speed before reaching 10 fruits  

while True:
    for event in pygame.event.get():
        # for the exit button
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == SCREEN_UPDATE:
            main_game.update()
        if event.type == pygame.KEYDOWN:
            # player inputs and directions action and if you wanted to play the game again you can if you want to quit press q
            if not main_game.is_game_over:
                if event.key == pygame.K_w and main_game.snake.direction.y != 1:
                    main_game.snake.direction = Vector2(0, -1)
                if event.key == pygame.K_s and main_game.snake.direction.y != -1:
                    main_game.snake.direction = Vector2(0, 1)
                if event.key == pygame.K_a and main_game.snake.direction.x != 1:
                    main_game.snake.direction = Vector2(-1, 0)
                if event.key == pygame.K_d and main_game.snake.direction.x != -1:
                    main_game.snake.direction = Vector2(1, 0)
            elif main_game.is_game_over:
                if event.key == pygame.K_r:
                    main_game.reset()
                elif event.key == pygame.K_q:
                    pygame.quit()
                    sys.exit()
    # screen size, fps, loading of the fruit and the player
    screen.fill((130, 220, 75))
    main_game.draw_elements()
    pygame.display.update()
    clock.tick(60)
