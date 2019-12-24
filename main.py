import pygame
pygame.init()

# screen
screen = pygame.display.set_mode((400, 400))

# player One
PlayerWidth = 100
PlayerHeight = 20
PlayerX = 200
PlayerY = 370
PlayerX_change = 0

# Enemy
EnemyWidth = 100
EnemyHeight = 20
EnemyX = 150
EnemyY = 10
Enemy_speed = -2

# ball
ballRadius = 10
BallX = 200
BallY = 200
Ball_XSPEED = 2
Ball_YSPEED = 2

# scoring
Enemy_points = 0
Player_points = 0
score_to_win = 5

# Scoring font
font = pygame.font.Font('freesansbold.ttf', 16)

# game over text
over_font = pygame.font.Font('freesansbold.ttf', 32)


def show_score(caption, x, y):
    score = font.render(caption, True, (0, 0, 0))
    screen.blit(score, (x, y))


def gameOver():
    game_over_sign = over_font.render(f"Game over: {score_to_win} points", True, (0, 0, 0))
    screen.blit(game_over_sign, (40, 165))


def playerOne(x, y, width, height):
    pygame.draw.rect(screen, (0, 0, 0), [x, y, width, height])


def enemy(x, y, width, height):
    pygame.draw.rect(screen, (0, 0, 0), [x, y, width, height])


def ball(radius, BallX, BallY):
    pygame.draw.circle(screen, (0, 0, 0), (BallX, BallY), radius)


playing = True
while playing:

    screen.fill((255, 255, 255))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            playing = False

        # player movement keys
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                PlayerX_change = 2
            if event.key == pygame.K_LEFT:
                PlayerX_change = -2
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT or event.key == pygame.K_LEFT:
                PlayerX_change = 0
    PlayerX += PlayerX_change

    # stops player from going of the left and right edge
    if PlayerX >= 390 - PlayerWidth:
        PlayerX = 390 - PlayerWidth
    elif PlayerX <= 10:
        PlayerX = 10

    # auto enemy movement
    EnemyX += Enemy_speed
    if EnemyX == 10:
        EnemyX += Enemy_speed
        Enemy_speed = 2
    elif EnemyX == 290:
        EnemyX += Enemy_speed
        Enemy_speed = -2

    # ball movement and wall collision X axis
    BallX += Ball_XSPEED
    if BallX == 10:
        BallX += Ball_XSPEED
        Ball_XSPEED = 2
    elif BallX == 400 - ballRadius:
        BallX += Ball_XSPEED
        Ball_XSPEED = -2

    # ball movement and wall collision Y axis
    BallY += Ball_YSPEED
    if BallY <= 10:
        BallY += Ball_YSPEED
        Ball_YSPEED = 2
    elif BallY >= 400 - ballRadius:
        BallY += Ball_YSPEED
        Ball_YSPEED = -2

    # enemy and player paddle ball collision
    if BallY >= PlayerY and (PlayerX + PlayerWidth >= BallX >= PlayerX):
        BallY += Ball_YSPEED * (-1)
        Ball_YSPEED = -2
    elif (BallY <= EnemyY + EnemyHeight) and (EnemyX + EnemyWidth >= BallX >= EnemyX):
        BallY += Ball_YSPEED * (-1)
        Ball_YSPEED = 2

     # player and enemy scoring
    if BallY >= 400 - ballRadius:
        Enemy_points += 1
    elif BallY <= ballRadius:
        Player_points += 1

    # points to win and scoring
    if Enemy_points >= score_to_win - 1 or Player_points >= score_to_win - 1:
        gameOver()
    if Enemy_points == score_to_win or Player_points == score_to_win:
        playing = False



    ball(ballRadius, BallX, BallY)
    playerOne(PlayerX, PlayerY, PlayerWidth, PlayerHeight)
    enemy(EnemyX, EnemyY, EnemyWidth, EnemyHeight)
    show_score((f"Enemy: " + str(Enemy_points)), 1, 280)
    show_score((f"Player: " + str(Player_points)), 1, 300)
    pygame.display.update()
