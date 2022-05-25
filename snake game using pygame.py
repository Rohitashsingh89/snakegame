import pygame
import sys
import time
import random

score = 0

def level1():
    difficulty = 10

    # Window size
    window_x = 720
    window_y = 480
    width = int(window_x / 1.6)

    # Checks for errors encountered
    check_errors = pygame.init()

    # Initialise game window
    pygame.display.set_caption('Snake Game')
    game_window = pygame.display.set_mode((window_x, window_y))

    # game_window.pygame.image.load('background image.png')

    black = pygame.Color(0, 0, 0)
    white = pygame.Color(255, 255, 255)
    red = pygame.Color(255, 0, 0)
    green = pygame.Color(0, 255, 0)
    
    # FPS (frames per second)
    fps_controller = pygame.time.Clock()


    # Game variables
    snake_pos = [100, 50]
    snake_body = [[100, 50], [90, 50], [80, 50], [70, 50], [60, 50], [50, 50]]

    food_pos = [random.randrange(1, (window_x//10)) * 10, random.randrange(1, (window_y//10)) * 10]
    food_spawn = True

    pygame.display.update()

    direction = 'RIGHT'
    change_to = direction

    score = 0

    barriers = pygame.draw.rect(
            game_window,
            (255, 255, 255),
            (window_x / 2, 100, 10,200)
        )
    pygame.mixer.music.load("music.mp3")
    pygame.mixer.music.play()

    # Game Over function
    def game_over():
        my_font = pygame.font.SysFont('times new roman', 90)
        game_over_surface = my_font.render('YOU DIED', True, red)
        game_over_rect = game_over_surface.get_rect()
        game_over_rect.midtop = (window_x/2, window_y/4)
        game_window.fill(black)
        game_window.blit(game_over_surface, game_over_rect)
        show_score(0, red, 'times', 20)
        pygame.display.flip()
        time.sleep(3)
        pygame.quit()
        sys.exit()


    # Show the Score
    def show_score(choice, color, font, size):
        score_font = pygame.font.SysFont(font, size)
        score_surface = score_font.render('Score : ' + str(score), True, color)
        score_surface1 = score_font.render('now level = 1(<=100) ', True, color)
        score_surface2 = score_font.render('Total 3 level ', True, color)
        # score_surface3 = score_font.render('level = 3(>200) ', True, color)
        score_rect = score_surface.get_rect()
        if choice == 1:
            score_rect.midtop = (window_x/10, 15)
            
            barriers = pygame.draw.rect(
                game_window,
                (255, 255, 255),
                (700 / 2 - 20, 100, 10,200)
            )
        else:
            score_rect.midtop = (window_x/2, window_y/1.25)
            pygame.mixer.music.pause()
        game_window.blit(score_surface, score_rect)
        game_window.blit(score_surface1, ((500, 20)))
        game_window.blit(score_surface2, ((550, 40)))


    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            #  when a key press
            elif event.type == pygame.KEYDOWN:
                # W -> Up; S -> Down; A -> Left; D -> Right
                if event.key == pygame.K_UP or event.key == ord('w'):
                    change_to = 'UP'
                if event.key == pygame.K_DOWN or event.key == ord('s'):
                    change_to = 'DOWN'
                if event.key == pygame.K_LEFT or event.key == ord('a'):
                    change_to = 'LEFT'
                if event.key == pygame.K_RIGHT or event.key == ord('d'):
                    change_to = 'RIGHT'
                # Ese to exit 
                if event.key == pygame.K_ESCAPE:
                    exit()

        # to stop snake to move opposite direction
        if change_to == 'UP' and direction != 'DOWN':
            direction = 'UP'
        if change_to == 'DOWN' and direction != 'UP':
            direction = 'DOWN'
        if change_to == 'LEFT' and direction != 'RIGHT':
            direction = 'LEFT'
        if change_to == 'RIGHT' and direction != 'LEFT':
            direction = 'RIGHT'

        # Moving the snake
        if direction == 'UP':
            snake_pos[1] -= 10
        if direction == 'DOWN':
            snake_pos[1] += 10
        if direction == 'LEFT':
            snake_pos[0] -= 10
        if direction == 'RIGHT':
            snake_pos[0] += 10

        # Increase snake size when hit the food
        snake_body.insert(0, list(snake_pos))
        if snake_pos[0] == food_pos[0] and snake_pos[1] == food_pos[1]:
            sound = pygame.mixer.Sound("food.mp3")
            pygame.mixer.Sound.play(sound)
            score += 10
            food_spawn = False
        else:
            snake_body.pop()

        # Spawning food on the screen
        if not food_spawn:
            food_pos = [random.randrange(1, (window_x//10)) * 10, random.randrange(1, (window_y//10)) * 10]
        food_spawn = True

        # fill the game window or GFX
        game_window.fill(black)
        for pos in snake_body:
            pygame.draw.rect(game_window, green, pygame.Rect(pos[0], pos[1], 10, 10))

        # Snake food
        pygame.draw.rect(game_window, red, pygame.Rect(food_pos[0], food_pos[1], 10, 10))

        
        # Game Over conditions
        # When snake hit the wall 
        if snake_pos[0] < 0 or snake_pos[0] > window_x-10:
            sound = pygame.mixer.Sound("gameover.mp3")
            pygame.mixer.Sound.play(sound)
            game_over()
        if snake_pos[1] < 0 or snake_pos[1] > window_y-10:
            sound = pygame.mixer.Sound("gameover.mp3")
            pygame.mixer.Sound.play(sound)
            game_over()
        if snake_pos[0] > barriers[0] -40 and snake_pos[0] < abs(barriers[0] -20) and snake_pos[1] > barriers[3] -110 and snake_pos[1] < abs(barriers[3] + 100): 
            sound = pygame.mixer.Sound("gameover.mp3")
            pygame.mixer.Sound.play(sound)
            game_over()

        # Touching the snake body
        for block in snake_body[1:]:
            if snake_pos[0] == block[0]  and snake_pos[1] == block[1]:
                game_over()

        show_score(1, white, 'consolas', 20) 
        # Refresh game screen
        pygame.display.update()
        # Refresh rate
        fps_controller.tick(difficulty)
        if score == 110:
            level2()

def level2():
        
    difficulty = 15

    # Window size
    window_x = 720
    window_y = 480
    width = int(window_x / 1.6)

    # Checks for errors encountered
    check_errors = pygame.init()

    # Initialise game window
    pygame.display.set_caption('Snake Game')
    game_window = pygame.display.set_mode((window_x, window_y))

    black = pygame.Color(0, 0, 0)
    white = pygame.Color(255, 255, 255)
    red = pygame.Color(255, 0, 0)
    green = pygame.Color(0, 255, 0)
    blue = pygame.Color(0, 0, 255)

    # FPS (frames per second)
    fps_controller = pygame.time.Clock()

    # Game variables
    snake_pos = [100, 50]
    snake_body = [[100, 50], [90, 50], [80, 50], [70, 50], [60, 50], [50, 50]]

    food_pos = [random.randrange(1, (window_x//10)-30) * 10, random.randrange(1, (window_y//10)-20) * 10]
    food_spawn = True

    pygame.display.update()

    direction = 'RIGHT'
    change_to = direction

    score = 0

    barriers2 = pygame.draw.rect(
            game_window,
            (255, 255, 255),
            (window_x / 4, 100, 10,200)
        )
    barriers3 = pygame.draw.rect(
            game_window,
            (255, 255, 255),
            (window_x / 1.5, 100, 10,200)
        )

    pygame.mixer.music.load("music.mp3")
    pygame.mixer.music.play()

    # Game Over function
    def game_over():
        my_font = pygame.font.SysFont('times new roman', 90)
        game_over_surface = my_font.render('YOU DIED', True, red)
        game_over_rect = game_over_surface.get_rect()
        game_over_rect.midtop = (window_x/2, window_y/4)
        game_window.fill(black)
        game_window.blit(game_over_surface, game_over_rect)
        show_score(0, red, 'times', 20)
        pygame.display.flip()
        time.sleep(3)
        pygame.quit()
        sys.exit()


    # Show the Score
    def show_score(choice, color, font, size):
        score_font = pygame.font.SysFont(font, size)
        score_surface = score_font.render('Score : ' + str(score), True, color)
        score_surface1 = score_font.render('level = 2 ', True, color)
        score_rect = score_surface.get_rect()
        if choice == 1:
            score_rect.midtop = (window_x/10, 15)
        
            barriers2 = pygame.draw.rect(
                game_window,
                (255, 255, 255),
                (window_x / 4, 100, 10,200)
            )
            barriers3 = pygame.draw.rect(
                game_window,
                (255, 255, 255),
                (window_x / 1.5, 100, 10,200)
            )
        else:
            score_rect.midtop = (window_x/2, window_y/1.25)
            pygame.mixer.music.pause()
        game_window.blit(score_surface, score_rect)
        game_window.blit(score_surface1, ((550, 20)))

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            #  when a key press
            elif event.type == pygame.KEYDOWN:
                # W -> Up; S -> Down; A -> Left; D -> Right
                if event.key == pygame.K_UP or event.key == ord('w'):
                    change_to = 'UP'
                if event.key == pygame.K_DOWN or event.key == ord('s'):
                    change_to = 'DOWN'
                if event.key == pygame.K_LEFT or event.key == ord('a'):
                    change_to = 'LEFT'
                if event.key == pygame.K_RIGHT or event.key == ord('d'):
                    change_to = 'RIGHT'
                # Ese to exit 
                if event.key == pygame.K_ESCAPE:
                    exit()

        # to stop snake to move opposite direction
        if change_to == 'UP' and direction != 'DOWN':
            direction = 'UP'
        if change_to == 'DOWN' and direction != 'UP':
            direction = 'DOWN'
        if change_to == 'LEFT' and direction != 'RIGHT':
            direction = 'LEFT'
        if change_to == 'RIGHT' and direction != 'LEFT':
            direction = 'RIGHT'

        # Moving the snake
        if direction == 'UP':
            snake_pos[1] -= 10
        if direction == 'DOWN':
            snake_pos[1] += 10
        if direction == 'LEFT':
            snake_pos[0] -= 10
        if direction == 'RIGHT':
            snake_pos[0] += 10

        # Increase snake size when hit the food
        snake_body.insert(0, list(snake_pos))
        if snake_pos[0] == food_pos[0] and snake_pos[1] == food_pos[1]:
            sound = pygame.mixer.Sound("food.mp3")
            pygame.mixer.Sound.play(sound)
            score += 10
            food_spawn = False
        else:
            snake_body.pop()

        # Spawning food on the screen
        if not food_spawn:
            food_pos = [random.randrange(1, (window_x//10)) * 10, random.randrange(1, (window_y//10)) * 10]
        food_spawn = True

        # fill the game window or GFX
        game_window.fill(black)
        for pos in snake_body:
            pygame.draw.rect(game_window, green, pygame.Rect(pos[0], pos[1], 10, 10))

        # Snake food
        pygame.draw.rect(game_window, red, pygame.Rect(food_pos[0], food_pos[1], 10, 10))

        
        # Game Over conditions
        # When snake hit the wall 
        if snake_pos[0] < 0 or snake_pos[0] > window_x-10:
            sound = pygame.mixer.Sound("gameover.mp3")
            pygame.mixer.Sound.play(sound)
            game_over()
        if snake_pos[1] < 0 or snake_pos[1] > window_y-10:
            sound = pygame.mixer.Sound("gameover.mp3")
            pygame.mixer.Sound.play(sound)
            game_over()
        if snake_pos[0] > barriers2[0] -10 and snake_pos[0] < abs(barriers2[0] +10) and snake_pos[1] > barriers2[3] -110 and snake_pos[1] < abs(barriers2[3] + 100): 
            sound = pygame.mixer.Sound("gameover.mp3")
            pygame.mixer.Sound.play(sound)
            game_over()
        if snake_pos[0] > barriers3[0] -10 and snake_pos[0] < abs(barriers3[0] +10) and snake_pos[1] > barriers3[3] -110 and snake_pos[1] < abs(barriers3[3] + 100): 
            sound = pygame.mixer.Sound("gameover.mp3")
            pygame.mixer.Sound.play(sound)
            game_over()

        # Touching the snake body
        for block in snake_body[1:]:
            if snake_pos[0] == block[0]  and snake_pos[1] == block[1]:
                game_over()

        show_score(1, white, 'consolas', 20)
        # Refresh game screen
        pygame.display.update()
        # Refresh rate
        fps_controller.tick(difficulty)

        if score == 100:
            level3()
    
def level3():
        
    difficulty = 20

    # Window size
    window_x = 720
    window_y = 480
    width = int(window_x / 1.6)

    # Checks for errors encountered
    check_errors = pygame.init()

    # Initialise game window
    pygame.display.set_caption('Snake Game')
    game_window = pygame.display.set_mode((window_x, window_y))



    black = pygame.Color(0, 0, 0)
    white = pygame.Color(255, 255, 255)
    red = pygame.Color(255, 0, 0)
    green = pygame.Color(0, 255, 0)
    blue = pygame.Color(0, 0, 255)


    # FPS (frames per second)
    fps_controller = pygame.time.Clock()


    # Game variables
    snake_pos = [100, 50]
    snake_body = [[100, 50], [90, 50], [80, 50], [70, 50], [60, 50], [50, 50]]

    food_pos = [random.randrange(1, (window_x//10)) * 10, random.randrange(1, (window_y//10)) * 10]
    food_spawn = True

    pygame.display.update()

    direction = 'RIGHT'
    change_to = direction

    score = 0

    barriers = pygame.draw.rect(
            game_window,
            (255, 255, 255),
            (window_x / 2, 100, 10,200)
        )
    barriers2 = pygame.draw.rect(
            game_window,
            (255, 255, 255),
            (window_x / 4, 100, 10,200)
        )
    barriers3 = pygame.draw.rect(
            game_window,
            (255, 255, 255),
            (window_x / 1.5, 100, 10,200)
        )

    pygame.mixer.music.load("music.mp3")
    pygame.mixer.music.play()
    

    # Game Over function
    def game_over():
        my_font = pygame.font.SysFont('times new roman', 90)
        game_over_surface = my_font.render('YOU DIED', True, red)
        game_over_rect = game_over_surface.get_rect()
        game_over_rect.midtop = (window_x/2, window_y/4)
        game_window.fill(black)
        game_window.blit(game_over_surface, game_over_rect)
        show_score(0, red, 'times', 20)
        pygame.display.flip()
        time.sleep(3)
        pygame.quit()
        sys.exit()


    # Show the Score
    def show_score(choice, color, font, size):
        score_font = pygame.font.SysFont(font, size)
        score_surface = score_font.render('Score : ' + str(score), True, color)
        score_surface1 = score_font.render('level = 3 ', True, color)
        score_rect = score_surface.get_rect()
        if choice == 1:
            score_rect.midtop = (window_x/10, 15)
            
            barriers2 = pygame.draw.rect(
                game_window,
                (255, 255, 255),
                (window_x / 4, 100, 10,200)
            )
            
            barriers3 = pygame.draw.rect(
                game_window,
                (255, 255, 255),
                (window_x / 1.5, 100, 10,200)
            )
            barriers = pygame.draw.rect(
                game_window,
                (255, 255, 255),
                (700 / 2 - 20, 100, 10,200)
            )

        else:
            score_rect.midtop = (window_x/2, window_y/1.25)
            pygame.mixer.music.pause()
        game_window.blit(score_surface, score_rect)
        game_window.blit(score_surface1, ((550, 20)))
                

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            #  when a key press
            elif event.type == pygame.KEYDOWN:
                # W -> Up; S -> Down; A -> Left; D -> Right
                if event.key == pygame.K_UP or event.key == ord('w'):
                    change_to = 'UP'
                if event.key == pygame.K_DOWN or event.key == ord('s'):
                    change_to = 'DOWN'
                if event.key == pygame.K_LEFT or event.key == ord('a'):
                    change_to = 'LEFT'
                if event.key == pygame.K_RIGHT or event.key == ord('d'):
                    change_to = 'RIGHT'
                # Ese to exit 
                if event.key == pygame.K_ESCAPE:
                    exit()

        # to stop snake to move opposite direction
        if change_to == 'UP' and direction != 'DOWN':
            direction = 'UP'
        if change_to == 'DOWN' and direction != 'UP':
            direction = 'DOWN'
        if change_to == 'LEFT' and direction != 'RIGHT':
            direction = 'LEFT'
        if change_to == 'RIGHT' and direction != 'LEFT':
            direction = 'RIGHT'

        # Moving the snake
        if direction == 'UP':
            snake_pos[1] -= 10
        if direction == 'DOWN':
            snake_pos[1] += 10
        if direction == 'LEFT':
            snake_pos[0] -= 10
        if direction == 'RIGHT':
            snake_pos[0] += 10

        # Increase snake size when hit the food
        snake_body.insert(0, list(snake_pos))
        if snake_pos[0] == food_pos[0] and snake_pos[1] == food_pos[1]:
            sound = pygame.mixer.Sound("food.mp3")
            pygame.mixer.Sound.play(sound)
            score += 10
            food_spawn = False
        else:
            snake_body.pop()

        # Spawning food on the screen
        if not food_spawn:
            food_pos = [random.randrange(1, (window_x//10)) * 10, random.randrange(1, (window_y//10)) * 10]
        food_spawn = True

        # fill the game window or GFX
        game_window.fill(black)
        for pos in snake_body:
            pygame.draw.rect(game_window, green, pygame.Rect(pos[0], pos[1], 10, 10))

        # Snake food
        pygame.draw.rect(game_window, red, pygame.Rect(food_pos[0], food_pos[1], 10, 10))

        
        # Game Over conditions
        # When snake hit the wall 
        if snake_pos[0] < 0 or snake_pos[0] > window_x-10:
            sound = pygame.mixer.Sound("gameover.mp3")
            pygame.mixer.Sound.play(sound)
            game_over()
        if snake_pos[1] < 0 or snake_pos[1] > window_y-10:
            sound = pygame.mixer.Sound("gameover.mp3")
            pygame.mixer.Sound.play(sound)
            game_over()
        if snake_pos[0] > barriers2[0] -10 and snake_pos[0] < abs(barriers2[0] +10) and snake_pos[1] > barriers2[3] -110 and snake_pos[1] < abs(barriers2[3] + 100):
            sound = pygame.mixer.Sound("gameover.mp3")
            pygame.mixer.Sound.play(sound) 
            game_over()
        if snake_pos[0] > barriers[0] -40 and snake_pos[0] < abs(barriers[0] -20) and snake_pos[1] > barriers[3] -110 and snake_pos[1] < abs(barriers[3] + 100): 
            sound = pygame.mixer.Sound("gameover.mp3")
            pygame.mixer.Sound.play(sound)
            game_over()
        if snake_pos[0] > barriers3[0] -10 and snake_pos[0] < abs(barriers3[0] +10) and snake_pos[1] > barriers3[3] -110 and snake_pos[1] < abs(barriers3[3] + 100): 
            sound = pygame.mixer.Sound("gameover.mp3")
            pygame.mixer.Sound.play(sound)
            game_over()

        # Touching the snake body
        for block in snake_body[1:]:
            if snake_pos[0] == block[0]  and snake_pos[1] == block[1]:
                game_over()

        show_score(1, white, 'consolas', 20)
        # Refresh game screen
        pygame.display.update()
        # Refresh rate
        fps_controller.tick(difficulty)


        if score == 100:
            level4()


def level4():
        
    difficulty = 20

    # Window size
    window_x = 720
    window_y = 480
    width = int(window_x / 1.6)

    # Checks for errors encountered
    check_errors = pygame.init()

    # Initialise game window
    pygame.display.set_caption('Snake Game')
    game_window = pygame.display.set_mode((window_x, window_y))



    black = pygame.Color(0, 0, 0)
    white = pygame.Color(255, 255, 255)
    red = pygame.Color(255, 0, 0)
    green = pygame.Color(0, 255, 0)
    blue = pygame.Color(0, 0, 255)


    # FPS (frames per second)
    fps_controller = pygame.time.Clock()


    # Game variables
    snake_pos = [100, 50]
    snake_body = [[100, 50], [90, 50], [80, 50], [70, 50], [60, 50], [50, 50]]

    food_pos = [random.randrange(1, (window_x//10)) * 10, random.randrange(1, (window_y//10)) * 10]
    food_spawn = True

    pygame.display.update()

    direction = 'RIGHT'
    change_to = direction

    score = 0


    # first bar or barriers or vertical bar
    barriers2 = pygame.draw.rect(
        game_window,
        (255, 255, 255),
        (window_x / 4, 100, 10,100)
    )
    # Horizontal barrier or bar 
    barriers = pygame.draw.rect(
        game_window,
        (255, 255, 255),
        (700 / 2 -110, 200, 200,10)
    )
    # second barrier or bar vertically
    barriers3 = pygame.draw.rect(
        game_window,
        (255, 255, 255),
        (window_x / 1.5, 100, 10,200)
    )
    pygame.mixer.music.load("music.mp3")
    pygame.mixer.music.play()
    

    # Game Over function
    def game_over():
        my_font = pygame.font.SysFont('times new roman', 90)
        game_over_surface = my_font.render('YOU DIED', True, red)
        game_over_rect = game_over_surface.get_rect()
        game_over_rect.midtop = (window_x/2, window_y/4)
        game_window.fill(black)
        game_window.blit(game_over_surface, game_over_rect)
        show_score(0, red, 'times', 20)
        pygame.display.flip()
        time.sleep(3)
        pygame.quit()
        sys.exit()


    # Show the Score
    def show_score(choice, color, font, size):
        score_font = pygame.font.SysFont(font, size)
        score_surface = score_font.render('Score : ' + str(score), True, color)
        score_surface1 = score_font.render('level = 3 ', True, color)
        score_rect = score_surface.get_rect()
        if choice == 1:
            score_rect.midtop = (window_x/10, 15)
            
                
            # first bar or barriers or vertical bar
            barriers2 = pygame.draw.rect(
                game_window,
                (255, 255, 255),
                (window_x / 4, 100, 10,100)
            )
            # Horizontal barrier or bar 
            barriers = pygame.draw.rect(
                game_window,
                (255, 255, 255),
                (700 / 2 -110, 200, 200,10)
            )
            # second barrier or bar vertically
            barriers3 = pygame.draw.rect(
                game_window,
                (255, 255, 255),
                (window_x / 1.5, 100, 10,200)
            )
        else:
            score_rect.midtop = (window_x/2, window_y/1.25)
            pygame.mixer.music.pause()
        game_window.blit(score_surface, score_rect)
        game_window.blit(score_surface1, ((550, 20)))
                

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            #  when a key press
            elif event.type == pygame.KEYDOWN:
                # W -> Up; S -> Down; A -> Left; D -> Right
                if event.key == pygame.K_UP or event.key == ord('w'):
                    change_to = 'UP'
                if event.key == pygame.K_DOWN or event.key == ord('s'):
                    change_to = 'DOWN'
                if event.key == pygame.K_LEFT or event.key == ord('a'):
                    change_to = 'LEFT'
                if event.key == pygame.K_RIGHT or event.key == ord('d'):
                    change_to = 'RIGHT'
                # Ese to exit 
                if event.key == pygame.K_ESCAPE:
                    exit()

        # to stop snake to move opposite direction
        if change_to == 'UP' and direction != 'DOWN':
            direction = 'UP'
        if change_to == 'DOWN' and direction != 'UP':
            direction = 'DOWN'
        if change_to == 'LEFT' and direction != 'RIGHT':
            direction = 'LEFT'
        if change_to == 'RIGHT' and direction != 'LEFT':
            direction = 'RIGHT'

        # Moving the snake
        if direction == 'UP':
            snake_pos[1] -= 10
        if direction == 'DOWN':
            snake_pos[1] += 10
        if direction == 'LEFT':
            snake_pos[0] -= 10
        if direction == 'RIGHT':
            snake_pos[0] += 10

        # Increase snake size when hit the food
        snake_body.insert(0, list(snake_pos))
        if snake_pos[0] == food_pos[0] and snake_pos[1] == food_pos[1]:
            sound = pygame.mixer.Sound("food.mp3")
            pygame.mixer.Sound.play(sound)
            score += 10
            food_spawn = False
        else:
            snake_body.pop()

        # Spawning food on the screen
        if not food_spawn:
            food_pos = [random.randrange(1, (window_x//10)) * 10, random.randrange(1, (window_y//10)) * 10]
        food_spawn = True

        # fill the game window or GFX
        game_window.fill(black)
        for pos in snake_body:
            pygame.draw.rect(game_window, green, pygame.Rect(pos[0], pos[1], 10, 10))

        # Snake food
        pygame.draw.rect(game_window, red, pygame.Rect(food_pos[0], food_pos[1], 10, 10))

            
            
        
        # Game Over conditions
        # When snake hit the wall 
        if snake_pos[0] < 0 or snake_pos[0] > window_x-10:
            sound = pygame.mixer.Sound("gameover.mp3")
            pygame.mixer.Sound.play(sound)
            game_over()
        if snake_pos[1] < 0 or snake_pos[1] > window_y-10:
            sound = pygame.mixer.Sound("gameover.mp3")
            pygame.mixer.Sound.play(sound)
            game_over()
        # collision logic for first bar or barriers or vertical bar
        if snake_pos[0] > barriers2[0] -10 and snake_pos[0] < abs(barriers2[0] +10) and snake_pos[1] > barriers2[3] -10 and snake_pos[1] < abs(barriers2[3] + 100): 
            sound = pygame.mixer.Sound("gameover.mp3")
            pygame.mixer.Sound.play(sound)
            game_over()
        # collision logic for Horizontal barrier or bar 
        if snake_pos[0] > barriers[0] -130 and snake_pos[0] < abs(barriers[0] +80) and snake_pos[1] > barriers[3] +90 and snake_pos[1] < abs(barriers[3] + 110): 
            sound = pygame.mixer.Sound("gameover.mp3")
            pygame.mixer.Sound.play(sound)
            game_over()
        # collision logic for second barrier or bar vertically
        if snake_pos[0] > barriers3[0] -10 and snake_pos[0] < abs(barriers3[0] +10) and snake_pos[1] > barriers3[3] -110 and snake_pos[1] < abs(barriers3[3] + 100): 
            sound = pygame.mixer.Sound("gameover.mp3")
            pygame.mixer.Sound.play(sound)
            game_over()

        # Touching the snake body
        for block in snake_body[1:]:
            if snake_pos[0] == block[0]  and snake_pos[1] == block[1]:
                game_over()

        show_score(1, white, 'consolas', 20)
        # Refresh game screen
        pygame.display.update()
        # Refresh rate
        fps_controller.tick(difficulty)


        if score == 100:
            score_font = pygame.font.SysFont('times', 30)
            game_over_surface = score_font.render('Congrates! You have successfully completed all levels ', True, red)
            game_over_rect = game_over_surface.get_rect()
            game_over_rect.midtop = (window_x/2, window_y/4)
            game_window.fill(black)
            game_window.blit(game_over_surface, game_over_rect)
            pygame.display.flip()
            pygame.mixer.music.pause()
            time.sleep(5)
            pygame.quit()
            sys.exit()
            
    

if score <= 100 and score >= 0:
    level1()
