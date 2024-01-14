import pygame

pygame.init()
clock = pygame.time.Clock()

screen = pygame.display.set_mode((1280, 720))
pygame.display.set_caption("Игра")
background = pygame.image.load("Images/back.jpg").convert()

'''Звуки'''

jump_sound = pygame.mixer.Sound("Sounds/jump.mp3")
bg_sound = pygame.mixer.Sound("Sounds/bg sound.mp3")
bg_sound.set_volume(4)
bg_sound.play()
shot_sound = pygame.mixer.Sound("Sounds/shot.mp3")
shot_sound.set_volume(5)
dead_sound = pygame.mixer.Sound("Sounds/dead.mp3")

walk_right = [
    pygame.image.load("Images/Игрок/Right move/move 1.png").convert_alpha(),
    pygame.image.load("Images/Игрок/Right move/move 2.png").convert_alpha(),
    pygame.image.load("Images/Игрок/Right move/move 3.png").convert_alpha()
]

walk_left = [
    pygame.image.load("Images/Игрок/Left move/move 1.png").convert_alpha(),
    pygame.image.load("Images/Игрок/Left move/move 2.png").convert_alpha(),
    pygame.image.load("Images/Игрок/Left move/move 3.png").convert_alpha()
]

ghost = pygame.image.load("Images/ghost.png").convert_alpha()
ghost_x = 1290

ghost_list_in_game = []

player_speed = 20
player_x = 0
player_y = 500
player_anim_count = 0

is_jump = False
jump_count = 10  # высота прыжка

ghost_timer = pygame.USEREVENT + 1
pygame.time.set_timer(ghost_timer, 3000)  # интервал спавна призраков

bullet = pygame.image.load("Images/bullet 1.png").convert_alpha()
bullets = []
bullets_left = 5  # кол-во пуль

'''Текст'''

label = pygame.font.Font("Fonts/RobotoCondensed-Black.ttf", 40)

play_label = label.render("Играть",False, (255, 255, 255))
play_label_rect = play_label.get_rect(topleft=(570, 250))

lose_label = label.render("Вы проиграли!", False, (255, 255, 255))

restart_label = label.render("Играть заново", False, (255, 255, 255))
restart_label_rect = restart_label.get_rect(topleft=(510, 400))

menu_button = label.render("Меню", False, (255, 255, 255))
menu_button_rect = menu_button.get_rect(topleft=(570, 500))


score = 0  # счет

def player_movement():
    global player_y, player_x, player_anim_count, is_jump, jump_count

    '''Перемещение героя'''

    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT]:
        screen.blit(walk_left[player_anim_count], (player_x, player_y))
    else:
        screen.blit(walk_right[player_anim_count], (player_x, player_y))

    if keys[pygame.K_RIGHT] and player_x < 1150:
        player_x += player_speed
    elif keys[pygame.K_LEFT] and player_x > 10:
        player_x -= player_speed

    if player_anim_count == len(walk_right) - 1:
        player_anim_count = 0
    else:
        player_anim_count += 1

    '''Прыжок'''

    if not is_jump:
        if keys[pygame.K_SPACE]:
            is_jump = True
    else:
        if jump_count >= -10:
            if jump_count > 0:
                player_y -= (jump_count ** 2) / 2
            elif jump_count == 0:
                jump_sound.play()
            else:
                player_y += (jump_count ** 2) / 2
            jump_count -= 1
        else:
            is_jump = False
            jump_count = 10


main_win = True  # стартовое окно


def you_lose():
    global score, gameplay, player_x, bullets_left, main_win

    '''Экран проигрыша'''

    bg_sound.stop()

    result_label = label.render("Результат: " + str(score), False, (255, 255, 255))

    screen.fill((143, 229, 255))
    screen.blit(lose_label, (510, 200))
    screen.blit(restart_label, restart_label_rect)
    screen.blit(result_label, (510, 300))
    screen.blit(menu_button, menu_button_rect)

    mouse = pygame.mouse.get_pos()  # координаты мыши

    if restart_label_rect.collidepoint(mouse) and pygame.mouse.get_pressed()[0]:
        gameplay = True
        player_x = 0
        score = 0
        ghost_list_in_game.clear()
        bullets.clear()
        bullets_left = 5
        bg_sound.play()


gameplay = False  # игровой процесс

lose_win = False #окно проигрыша

flag = True  # основной цикл

while flag:
    pygame.display.update()

    screen.blit(background, (0, 0))

    '''Игровой процесс'''

    if main_win:
        screen.blit(background, (0, 0))
        screen.blit(play_label, play_label_rect)
    elif gameplay:
        score_label = label.render("Счет: " + str(score), False, (255, 255, 255))
        patron_label = label.render("Осталось патронов: " + str(bullets_left), False, (255, 255, 255))

        screen.blit(score_label, (1100, 0))
        screen.blit(patron_label, (0, 0))

        '''Столкновение'''

        player_rect = walk_right[0].get_rect(topleft=(player_x, player_y))  # воображаемый квадрат игрока

        if ghost_list_in_game:
            for (i, el) in enumerate(ghost_list_in_game):
                screen.blit(ghost, el) # спавн призрака за экраномыы
                el.x -= 10
                if player_rect.colliderect(el):  # столкновение игрока с призраком
                    gameplay = False
                    lose_win = True
                    main_win = False

        player_movement()

        '''пули'''

        if bullets:
            for (i, el) in enumerate(bullets):
                screen.blit(bullet, (el.x, el.y))
                el.x += 10

                if el.x > 1290:
                    bullets.pop(i)

                '''Уничтожение призрака и пули'''

                if ghost_list_in_game:
                    for (index, ghosty) in enumerate(ghost_list_in_game):
                        if el.colliderect(ghosty):
                            bullets.pop(i)
                            ghost_list_in_game.pop(index)
                            dead_sound.play()
        score += 1
    elif lose_win:
        you_lose()

    mouse = pygame.mouse.get_pos()

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            flag = False
            pygame.quit()

        if event.type == ghost_timer:
            ghost_list_in_game.append(ghost.get_rect(topleft=(1290, 530)))

        if gameplay and event.type == pygame.KEYUP and event.key == pygame.K_v and bullets_left > 0:
            shot_sound.play()
            bullets.append(bullet.get_rect(topleft=(player_x + 30, player_y + 30)))
            bullets_left -= 1

        if main_win and play_label_rect.collidepoint(mouse) and pygame.mouse.get_pressed()[0]:  # событие нажатия на кнопку играть
            gameplay = True
            main_win = False

        if lose_win and menu_button_rect.collidepoint(mouse) and pygame.mouse.get_pressed()[0]:  # событие нажатия кнопку меню
            lose_win = False
            main_win = True
            gameplay = True
            player_x = 0
            score = 0
            ghost_list_in_game.clear()
            bullets.clear()
            bullets_left = 5
            bg_sound.play()

    clock.tick(25)