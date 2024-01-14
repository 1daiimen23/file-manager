import pygame
import os

os.chdir("The game")

pygame.init()
clock = pygame.time.Clock()

screen = pygame.display.set_mode((1280, 720))
pygame.display.set_caption("Игра")
background = pygame.image.load("Images/back.jpg").convert()
flag = True

main_player_walk_right = [
    pygame.image.load("Images/Игрок/Right move/move 1.png").convert_alpha(),
    pygame.image.load("Images/Игрок/Right move/move 2.png").convert_alpha(),
    pygame.image.load("Images/Игрок/Right move/move 3.png").convert_alpha()
]

main_player_walk_left = [
    pygame.image.load("Images/Игрок/Left move/move 1.png").convert_alpha(),
    pygame.image.load("Images/Игрок/Left move/move 2.png").convert_alpha(),
    pygame.image.load("Images/Игрок/Left move/move 3.png").convert_alpha()
]

main_menu = True
gameplay = False
lose_win = False

class Player():
    def __init__(self, walk_right, walk_left):
        self.walk_right = walk_right
        self.walk_left = walk_left
        self.player_x = 0
        self.player_y = 500
        self.player_anim_count = 0
        self.speed = 20
        self.is_jump = False
        self.jump_count = 10
        self.player_rect = self.walk_right[self.player_anim_count].get_rect(topleft=(self.player_x, self.player_y))

    def show_player(self):
        pass
        screen.blit(main_player_walk_right[0], (self.player_x, self.player_y))

    def move_player(self):
        global keys

        keys = pygame.key.get_pressed()

        if keys[pygame.K_LEFT]:
            screen.blit(main_player_walk_left[self.player_anim_count], (self.player_x, self.player_y))
        else:
            screen.blit(main_player_walk_right[self.player_anim_count], (self.player_x, self.player_y))

        if keys[pygame.K_RIGHT] and self.player_x < 1150:
            self.player_x += self.speed
        elif keys[pygame.K_LEFT] and self.player_x > 10:
            self.player_x -= self.speed

        if self.player_anim_count == len(main_player_walk_right) - 1:
            self.player_anim_count = 0
        else:
            self.player_anim_count += 1

    def jump(self):
        if not self.is_jump:
            if keys[pygame.K_SPACE]:
                self.is_jump = True
        else:
            if self.jump_count >= -10:
                if self.jump_count > 0:
                    self.player_y -= (self.jump_count ** 2) / 2
                else:
                    self.player_y += (self.jump_count ** 2) / 2
                self.jump_count -= 1
            else:
                self.is_jump = False
                self.jump_count = 10


main_player = Player(main_player_walk_right, main_player_walk_left)
class Enemy():
    def __init__(self, enemy_x, enemy_y, enemy_list_in_game, path_to_pic, time):
        self.enemy_x = enemy_x
        self.enemy_y = enemy_y
        self.enemy_list_in_game = enemy_list_in_game
        self.enemy = pygame.image.load(path_to_pic).convert_alpha()
        self.enemy_timer = pygame.USEREVENT + 1
        pygame.time.set_timer(self.enemy_timer, time)

    def spawn_enemy_and_meeting_with_player(self):
        global gameplay, lose_win, main_menu

        if self.enemy_list_in_game:
            for (i, el) in enumerate(self.enemy_list_in_game):
                screen.blit(self.enemy, el)  # спавн призрака за экраномыы
                el.x -= 10
                if main_player.player_rect.colliderect(el):  # столкновение игрока с призраком
                    gameplay = False
                    lose_win = True
                    main_menu = False


ghost_list_in_game = []
ghost = Enemy(1290, 530, ghost_list_in_game, "Images/ghost.png", 1000)

label = pygame.font.Font("Fonts/RobotoCondensed-Black.ttf", 40)
class Menu():
    def __init__(self):
        self.play_label = label.render("Играть", False, (255, 255, 255))
        self.play_label_rect = self.play_label.get_rect(topleft=(570, 250))

    def show(self):
        screen.blit(self.play_label, self.play_label_rect)


menu = Menu()


while flag:
    screen.blit(background, (0, 0))

    if main_menu:
        mouse = pygame.mouse.get_pos()
        menu.show()
    elif gameplay:
        main_player.move_player()
        main_player.jump()
        ghost.spawn_enemy_and_meeting_with_player()

    pygame.display.update()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            flag = False
            pygame.quit()

        if event.type == ghost.enemy_timer:
            ghost_list_in_game.append(ghost.enemy.get_rect(topleft=(ghost.enemy_x, ghost.enemy_y)))

        if main_menu and menu.play_label_rect.collidepoint(mouse) and pygame.mouse.get_pressed()[0]:
            main_menu = False
            gameplay = True

    clock.tick(25)

