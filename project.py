import pygame
from sys import exit


pygame.init()
screen = pygame.display.set_mode((800, 480))
pygame.display.set_caption("Catventure")
icon = pygame.image.load("cat-icon.png").convert()
pygame.display.set_icon(icon)
clock = pygame.time.Clock()
test_font = pygame.font.Font('font/PixelPowerline-11Mg.ttf', 50)
game_active = False
start_time = 0
score = 0

# screen media
woods_surface = pygame.image.load("woods.png").convert()

# intro screen
cat_stand = pygame.image.load('cat_1.png').convert_alpha()
cat_stand = pygame.transform.rotozoom(cat_stand, 0, 1.5)
cat_stand_rect = cat_stand.get_rect(center=(400, 240))

# game name
game_name = test_font.render('Catventure', False, (125, 74, 176))
game_name_rect = game_name.get_rect(center=(400, 80))

game_message = test_font.render('Press "space" to start', False, (125, 74, 176))
game_message_rect = game_message.get_rect(center=(400, 400))


def display_score(start_time, test_font, screen):
    current_time = int(pygame.time.get_ticks() / 1000) - start_time
    score_surface = test_font.render(f'Score: {current_time}', False, (125, 74, 176))
    score_rect = score_surface.get_rect(center=(400, 80))
    screen.blit(score_surface, score_rect)
    return current_time


class Cat:
    def __init__(self):
        self.cat_step_1 = pygame.image.load('cat_1.png').convert_alpha()
        self.cat_step_2 = pygame.image.load('new_cat2.png').convert_alpha()
        self.cat_step = [self.cat_step_1, self.cat_step_2]
        self.cat_jump = pygame.image.load('cat_jump.png').convert_alpha()
        self.cat_index = 0
        self.cat_gravity = 0

        self.cat_surface = self.cat_step[self.cat_index]
        self.cat_rect = self.cat_surface.get_rect(topleft=(100, 290))

    def cat_animation(self):
        if self.cat_rect.bottom < 430:
            self.cat_surface = self.cat_jump
        else:
            self.cat_index += 0.1
            if self.cat_index >= len(self.cat_step):
                self.cat_index = 0
            self.cat_surface = self.cat_step[int(self.cat_index)]

class Drop:
    def __init__(self):
        self.drop_f1 = pygame.transform.rotozoom(pygame.image.load('drop1.png').convert_alpha(), 0, 0.5)
        self.drop_f2 = pygame.transform.rotozoom(pygame.image.load('drop2.png').convert_alpha(), 0, 0.5)
        self.drop = [self.drop_f1, self.drop_f2]
        self.drop_index = 0

        self.drop_surface = self.drop[self.drop_index]
        self.drop_rect = self.drop_surface.get_rect(bottomright=(1600, 430))

    def drop_animation(self):
        self.drop_index += 0.1
        if self.drop_index >= len(self.drop):
            self.drop_index = 0
        self.drop_surface = self.drop[int(self.drop_index)]

def main():
    global game_active, start_time, score
    jump_drop = Drop()
    my_cat = Cat()
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if game_active:
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE and my_cat.cat_rect.bottom >= 430:
                        my_cat.cat_gravity = -20
            else:
                if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                    game_active = True
                    jump_drop.drop_rect.left = 800
                    start_time = int(pygame.time.get_ticks() / 1000)

        if game_active:
            screen.blit(woods_surface, (0, 0))
            score = display_score(start_time, test_font, screen)

            jump_drop.drop_rect.x -= 7
            if jump_drop.drop_rect.right <= 0:
                jump_drop.drop_rect.left = 800
            jump_drop.drop_animation()
            screen.blit(jump_drop.drop_surface, jump_drop.drop_rect)


            my_cat.cat_gravity += 1
            my_cat.cat_rect.y += my_cat.cat_gravity
            if my_cat.cat_rect.bottom >= 430:
                my_cat.cat_rect.bottom = 430
            my_cat.cat_animation()
            screen.blit(my_cat.cat_surface, my_cat.cat_rect)

            if jump_drop.drop_rect.colliderect(my_cat.cat_rect):
                game_active = False
        else:
            screen.fill((20, 5, 54))
            screen.blit(cat_stand, cat_stand_rect)
            screen.blit(game_name, game_name_rect)

            score_message = test_font.render(f'Score: {score}', False, (125, 74, 176))
            score_message_rect = score_message.get_rect(center=(400, 400))

            if score == 0:
                screen.blit(game_message, game_message_rect)
            else:
                screen.blit(score_message, score_message_rect)

        pygame.display.update()
        clock.tick(60)

if __name__ == "__main__":
    main()
