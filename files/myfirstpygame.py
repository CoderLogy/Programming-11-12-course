import pygame
import os
pygame.font.init()
pygame.mixer.init()
GREEN = (0,255,0)
WIDTH,HEIGHT = 900,600
SPACESHIP_WIDTH, SPACESHIP_HEIGHT = 55,40
WINDOW = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("First Game")
HEALTH_FONT = pygame.font.SysFont('comicsans', 40)
BULLET_FIRE_SOUND = pygame.mixer.Sound('Assets/Gun+Silencer.mp3')
PLAYER_WIN_SOUND = pygame.mixer.Sound('Assets/Applause.mp3' )
FPS = 60
BLACK = (0,0,0)
RED = (255,0,0)
YELLOW = (255,255,0)
WHITE = (255,255,255)
BULLET_SPEED = 7
YELLOW_HIT = pygame.USEREVENT + 1
RED_HIT = pygame.USEREVENT + 2
WINNER_TEXT = ""
RED_HEALTH = 10
YELLOW_HEALTH = 10
YELLOW_BULLET = []
RED_BULLET = []
MAX_BULLET = 3
BORDER = pygame.Rect(0,HEIGHT//2,WIDTH,10)
SPEED = 3
YELLOW_SPACESHIP_IMAGE = pygame.image.load(os.path.join('Assets', 'spaceship_yellow.png'))
YELLOW_SPACESHIP = pygame.transform.rotate(pygame.transform.scale(YELLOW_SPACESHIP_IMAGE, (SPACESHIP_WIDTH,SPACESHIP_HEIGHT)), 0)
RED_SPACESHIP_IMAGE = pygame.image.load(os.path.join('Assets', 'spaceship_red.png'))
RED_SPACESHIP = pygame.transform.rotate(pygame.transform.scale(RED_SPACESHIP_IMAGE, (SPACESHIP_WIDTH,SPACESHIP_HEIGHT)), 180)

def draw_window(red,yellow,RED_HEALTH,YELLOW_HEALTH):
    WINDOW.fill(GREEN)
    pygame.draw.rect(WINDOW, BLACK, BORDER)
    redHealthText = HEALTH_FONT.render("Health: "+ str(RED_HEALTH), 1, WHITE)
    yellowHealthText = HEALTH_FONT.render("Health: "+ str(YELLOW_HEALTH), 1, WHITE)
    WINDOW.blit(yellowHealthText, (WIDTH - yellowHealthText.get_width() - 10, 10))
    WINDOW.blit(redHealthText, (10, 325))
    for bullet in YELLOW_BULLET:
        pygame.draw.rect(WINDOW,YELLOW,bullet)
    for bullet in RED_BULLET:
        pygame.draw.rect(WINDOW,RED,bullet)
    WINDOW.blit(YELLOW_SPACESHIP, (yellow.x,yellow.y))
    WINDOW.blit(RED_SPACESHIP, (red.x,red.y))
    pygame.display.update()

def red_handle_movement(keysPressed,red):
    if keysPressed[pygame.K_w] and red.y - SPEED > BORDER.y + BORDER.height:
            red.y -= SPEED
    if keysPressed[pygame.K_s] and red.y + SPEED + red.height < HEIGHT:
            red.y += SPEED
    if keysPressed[pygame.K_a] and red.x - SPEED > 0:
            red.x -= SPEED
    if keysPressed[pygame.K_d] and red.x + SPEED + red.width < WIDTH:
            red.x += SPEED
def yellow_handle_movement(keysPressed, yellow):
    if keysPressed[pygame.K_UP] and yellow.y - SPEED > 0:
        yellow.y -= SPEED  # Move up

    if keysPressed[pygame.K_DOWN] and yellow.y + SPEED + yellow.height < BORDER.y:
        yellow.y += SPEED  # Move down but not past the BORDER

    if keysPressed[pygame.K_LEFT] and yellow.x - SPEED > 0:
        yellow.x -= SPEED  # Move left

    if keysPressed[pygame.K_RIGHT] and yellow.x + SPEED + yellow.width < WIDTH:
        yellow.x += SPEED  # Move right
def handle_bullets(YELLOW_BULLET, RED_BULLET, yellow, red):
    for bullet in YELLOW_BULLET[:]:
        bullet.y += BULLET_SPEED  # Yellow bullets go down
        if red.colliderect(bullet):
            pygame.event.post(pygame.event.Event(RED_HIT))
            YELLOW_BULLET.remove(bullet)
        elif bullet.y > HEIGHT:
            YELLOW_BULLET.remove(bullet)

    for bullet in RED_BULLET[:]:
        bullet.y -= BULLET_SPEED  # Red bullets go up
        if yellow.colliderect(bullet):
            pygame.event.post(pygame.event.Event(YELLOW_HIT))
            RED_BULLET.remove(bullet)
        elif bullet.y < 0:
            RED_BULLET.remove(bullet)

def draw_winner(text):
    draw_text = HEALTH_FONT.render(text,1, WHITE)
    WINDOW.blit(draw_text, (WIDTH//2 - draw_text.get_width()//2, HEIGHT//2 - draw_text.get_height()//2))
    pygame.display.update()

def main():
    global RED_HEALTH, YELLOW_HEALTH, WINNER_TEXT
    yellow = pygame.Rect(425,100,SPACESHIP_WIDTH,SPACESHIP_HEIGHT)
    red = pygame.Rect(425,400,SPACESHIP_WIDTH,SPACESHIP_HEIGHT)
    clock = pygame.time.Clock()
    run = True
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LCTRL and len(YELLOW_BULLET) < MAX_BULLET:
                    bullet = pygame.Rect(yellow.x + yellow.width - 30, yellow.y + yellow.height, 5,10)
                    YELLOW_BULLET.append(bullet)
                    BULLET_FIRE_SOUND.play()
                if event.key == pygame.K_RCTRL and len(RED_BULLET) < MAX_BULLET:
                    bullet = pygame.Rect(red.x + red.width - 30, red.y + red.height, 5,10)
                    RED_BULLET.append(bullet)
                    BULLET_FIRE_SOUND.play()
                if event.key == pygame.K_END:
                     main()
            if event.type == RED_HIT:
                RED_HEALTH -= 1
            if event.type == YELLOW_HIT:
                YELLOW_HEALTH -= 1
        if RED_HEALTH <= -1:
            WINNER_TEXT = "Yellow Wins!"
        if YELLOW_HEALTH <= -1:
            WINNER_TEXT = "Red Wins!"
        if WINNER_TEXT != "":
            draw_winner(WINNER_TEXT)
            PLAYER_WIN_SOUND.play()
            pygame.time.delay(3500)
            break
        keysPressed = pygame.key.get_pressed()
        handle_bullets(YELLOW_BULLET,RED_BULLET,yellow,red)
        red_handle_movement(keysPressed,red)
        yellow_handle_movement(keysPressed,yellow)
        draw_window(red,yellow,RED_HEALTH,YELLOW_HEALTH)
    pygame.quit()

if __name__ == "__main__":
    main()