import pygame
import random
pygame.init()
# colors
white = (255, 255, 255)
red = (255, 0, 0)
black = (0, 0, 0)
green = (0, 255, 0)

screen_width = 600
screen_height = 400
# Creating Window
gameWindow = pygame.display.set_mode((screen_width , screen_height))

pygame.display.set_caption("Snake")
pygame.display.update()
font = pygame.font.SysFont("Times New Roman", 17)


def wall_collision(snake_x,snake_y,screen_width,screen_height, game_over):
    if(snake_x>screen_width or snake_x<0 or snake_y>screen_height or snake_y<0):
        game_over = True
        print("Game Over")
    return game_over
def text_screen(text,color,x,y):
    screen_text=font.render(text,True,color)
    gameWindow.blit(screen_text,[x,y])
def plot_snake(gameWindow,black,head_list, snake_size):
    for x,y in head_list:
        pygame.draw.rect(gameWindow, green, [x,y, snake_size, snake_size])


# Game loop
def gameloop():
    # Game Variables
    exit_game = False
    game_over = False
    snake_x = 45
    snake_y = 55
    snake_size = 10
    food_size = 7
    clock = pygame.time.Clock()
    fps = 60
    velocity_x = 0
    velocity_y = 0
    init_velocity = 1
    food_x = random.randint(20, screen_width - 20)
    food_y = random.randint(20, screen_height - 20)
    score = 0

    head_list = []
    snake_length = 1

    with open("highscore.txt", "r") as f:
        highscore = f.read()

    while not exit_game:
        if game_over:
            with open("highscore.txt", "w") as f:
                f.write(str(highscore))
            gameWindow.fill(black)
            text_screen("Game Over Buddy! Press Enter To Continue",green,150,160)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit_game=True
                if event.type==pygame.KEYDOWN:
                    if event.key==pygame.K_RETURN:
                        gameloop()
        else:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit_game=True
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RIGHT:
                        velocity_x=init_velocity
                        velocity_y=0
                    if event.key == pygame.K_LEFT:
                        velocity_x=-init_velocity
                        velocity_y=0
                    if event.key == pygame.K_UP:
                        velocity_y=-init_velocity
                        velocity_x=0
                    if event.key == pygame.K_DOWN:
                        velocity_y=init_velocity
                        velocity_x=0
            snake_x+=velocity_x
            snake_y+=velocity_y

            if abs(snake_x-food_x)<6 and abs(snake_y-food_y)<6:
                score+=10
                if score>int(highscore):
                    highscore=score
                print("Score:",score)
                # text_screen("SCORE:"+str(score),red,5,5)
                food_x = random.randint(20, screen_width-20)
                food_y = random.randint(20, screen_height-20)
                snake_length+=10


            gameWindow.fill(black)
            text_screen("Score:" + str(score), red, 15, 1)
            text_screen("HighScore: "+str(highscore) , red,480,1)
            # pygame.draw.rect(gameWindow, red, [food_x, food_y], food_size)
            # pygame.draw.circle(gameWindow,red,(food_x,food_y),food_size)
            pygame.draw.rect(gameWindow, red, [food_x, food_y, food_size, food_size])
            head=[]
            head.append(snake_x)
            head.append(snake_y)
            head_list.append(head)

            if len(head_list)>snake_length:
                del head_list[0]
            if head in head_list[:-1]:
                game_over=True

            game_over=wall_collision(snake_x, snake_y, screen_width, screen_height, game_over)
            # pygame.draw.rect(gameWindow,black,[snake_x, snake_y, snake_size, snake_size])
            plot_snake(gameWindow,black,head_list,snake_size)

        pygame.display.update()
        clock.tick(fps)

    pygame.quit()
    quit()
gameloop()
