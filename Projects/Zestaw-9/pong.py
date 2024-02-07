import pygame
import sys
import random

pygame.init()

WIDTH, HEIGHT = 800, 600
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
FPS = 60

BUTTON_WIDTH, BUTTON_HEIGHT = 225, 75
BUTTON_COLOR = (81, 0, 212)
BUTTON_HOVER_COLOR = (0, 219, 139)
BUTTON_TEXT_COLOR = (225, 225, 225)
BUTTON_HOVER_TEXT_COLOR = BLACK

GAME_MODE_1_PLAYER = 1
GAME_MODE_2_PLAYERS = 2
PLAYER_SIDE_LEFT = "left"
PLAYER_SIDE_RIGHT = "right"
PLAYER_SIDE_BOTH = "both"

PLAYER_WIDTH, PLAYER_HEIGHT = 15, 100
PLAYER_SPEED = 7
BALL_RADIUS = 20
BALL_SPEED = 6

MAX_POINTS = 5

class Button:
    def __init__(self, x, y, width, height, color, hover_color, font, text, text_color, hover_text_color):
        self.rect = pygame.Rect(x, y, width, height)
        self.color = color
        self.hover_color = hover_color
        self.font = font
        self.text = text
        self.text_color = text_color
        self.hover_text_color = hover_text_color

    def draw(self, screen):
        pygame.draw.rect(screen, self.color, self.rect)
        text_render = self.font.render(self.text, True, self.text_color)
        text_rect = text_render.get_rect(center=self.rect.center)
        screen.blit(text_render, text_rect)

    def is_hovered(self, pos):
        return self.rect.collidepoint(pos)

class GameModeScreen:
    def __init__(self):
        self.button_font = pygame.font.Font(None, 45)
        self.info_font = pygame.font.Font(None, 25)
        self.mode_1_button = Button((WIDTH // 2) - (BUTTON_WIDTH // 2), 150, BUTTON_WIDTH, BUTTON_HEIGHT, BUTTON_COLOR, BUTTON_HOVER_COLOR, self.button_font, "1 Player", BUTTON_TEXT_COLOR, BUTTON_HOVER_TEXT_COLOR)
        self.mode_2_button = Button((WIDTH // 2) - (BUTTON_WIDTH // 2), 250, BUTTON_WIDTH, BUTTON_HEIGHT, BUTTON_COLOR, BUTTON_HOVER_COLOR, self.button_font, "2 Players", BUTTON_TEXT_COLOR, BUTTON_HOVER_TEXT_COLOR)
        self.info_1_text = self.info_font.render("Left Player - W, S", True, WHITE)
        self.info_2_text = self.info_font.render("Right Player - arrows", True, WHITE)

    def handle_input(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit(0)
        
        mouse_pos = pygame.mouse.get_pos()

        if pygame.mouse.get_pressed()[0] and self.mode_1_button.is_hovered(mouse_pos):
            pygame.time.delay(300)
            return ChoosePlayerScreen(GAME_MODE_1_PLAYER)
        
        if pygame.mouse.get_pressed()[0] and self.mode_2_button.is_hovered(mouse_pos):
            pygame.time.delay(200)
            return GameScreen(GAME_MODE_2_PLAYERS, PLAYER_SIDE_BOTH)

    def update(self):
        mouse_pos = pygame.mouse.get_pos()

        if self.mode_1_button.is_hovered(mouse_pos):
            self.mode_1_button.color = self.mode_1_button.hover_color
            self.mode_1_button.text_color = self.mode_1_button.hover_text_color
        else:
            self.mode_1_button.color = BUTTON_COLOR
            self.mode_1_button.text_color = BUTTON_TEXT_COLOR
        
        if self.mode_2_button.is_hovered(mouse_pos):
            self.mode_2_button.color = self.mode_2_button.hover_color
            self.mode_2_button.text_color = self.mode_2_button.hover_text_color
        else:
            self.mode_2_button.color = BUTTON_COLOR
            self.mode_2_button.text_color = BUTTON_TEXT_COLOR

    def render(self, screen):
        screen.fill(BLACK)
        self.mode_1_button.draw(screen)
        self.mode_2_button.draw(screen)
        screen.blit(self.info_1_text, ((WIDTH // 2) - (self.info_1_text.get_width() // 2), 450))
        screen.blit(self.info_2_text, ((WIDTH // 2) - (self.info_2_text.get_width() // 2), 500))
        pygame.display.flip()

class ChoosePlayerScreen:
    def __init__(self, game_mode):
        self.game_mode = game_mode
        self.font = pygame.font.Font(None, 45)
        self.button_left = Button((WIDTH // 2) - (BUTTON_WIDTH // 2), 225 - (BUTTON_HEIGHT // 2), BUTTON_WIDTH, BUTTON_HEIGHT, BUTTON_COLOR, BUTTON_HOVER_COLOR, self.font, "Left", BUTTON_TEXT_COLOR, BUTTON_HOVER_TEXT_COLOR)
        self.button_right = Button((WIDTH // 2) - (BUTTON_WIDTH // 2), 375 - (BUTTON_HEIGHT // 2), BUTTON_WIDTH, BUTTON_HEIGHT, BUTTON_COLOR, BUTTON_HOVER_COLOR, self.font, "Right", BUTTON_TEXT_COLOR, BUTTON_HOVER_TEXT_COLOR)

    def handle_input(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit(0)
        
        mouse_pos = pygame.mouse.get_pos()

        if pygame.mouse.get_pressed()[0] and self.button_left.is_hovered(mouse_pos):
            pygame.time.delay(200)
            return GameScreen(self.game_mode, PLAYER_SIDE_LEFT)
        
        if pygame.mouse.get_pressed()[0] and self.button_right.is_hovered(mouse_pos):
            pygame.time.delay(200)
            return GameScreen(self.game_mode, PLAYER_SIDE_RIGHT)

    def update(self):
        mouse_pos = pygame.mouse.get_pos()

        if self.button_left.is_hovered(mouse_pos):
            self.button_left.color = self.button_left.hover_color
            self.button_left.text_color = self.button_left.hover_text_color
        else:
            self.button_left.color = BUTTON_COLOR
            self.button_left.text_color = BUTTON_TEXT_COLOR
        
        if self.button_right.is_hovered(mouse_pos):
            self.button_right.color = self.button_right.hover_color
            self.button_right.text_color = self.button_right.hover_text_color
        else:
            self.button_right.color = BUTTON_COLOR
            self.button_right.text_color = BUTTON_TEXT_COLOR

    def render(self, screen):
        screen.fill(BLACK)
        self.button_left.draw(screen)
        self.button_right.draw(screen)
        pygame.display.flip()

class GameScreen:
    def __init__(self, game_mode, player_side):
        self.game_mode = game_mode
        self.player_side = player_side
        self.player_left = pygame.Rect(50, (HEIGHT // 2) - (PLAYER_HEIGHT // 2), PLAYER_WIDTH, PLAYER_HEIGHT)
        self.player_right = pygame.Rect(WIDTH - 50 - PLAYER_WIDTH, (HEIGHT // 2) - (PLAYER_HEIGHT // 2), PLAYER_WIDTH, PLAYER_HEIGHT)
        self.ball = pygame.Rect((WIDTH // 2) - (BALL_RADIUS // 2), (HEIGHT // 2) - (BALL_RADIUS // 2), BALL_RADIUS, BALL_RADIUS)
        self.ball_velocity = [BALL_SPEED, BALL_SPEED]
        self.short_break = False
        self.short_break_start = None
        self.short_break_stopwatch = None
        self.player_left_score = 0
        self.player_right_score = 0
        self.font = pygame.font.Font(None, 45)
        self.game_over = False

        self.ball_velocity[0] *= random.choice([1, -1])
        self.ball_velocity[1] *= random.choice([1, -1])
    
    def handle_input(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit(0)
            elif event.type == pygame.USEREVENT:
                print("Player left: " + event.left)
                print("Player right: " + event.right)
                print()
                pygame.time.delay(3000)
                return GameModeScreen()
        
        keys_pressed = pygame.key.get_pressed()

        if self.game_mode == GAME_MODE_1_PLAYER and self.player_side == PLAYER_SIDE_LEFT:
            if keys_pressed[pygame.K_w]:
                if self.player_left.top > 0:
                    self.player_left.y -= PLAYER_SPEED
            if keys_pressed[pygame.K_s]:
                if self.player_left.bottom < HEIGHT:
                    self.player_left.y += PLAYER_SPEED
            if self.ball_velocity[0] > 0:
                if self.player_right.centery > self.ball.centery:
                    self.player_right.y -= (PLAYER_SPEED - 3)
                if self.player_right.centery < self.ball.centery:
                    self.player_right.y += (PLAYER_SPEED - 3)
        
        if self.game_mode == GAME_MODE_1_PLAYER and self.player_side == PLAYER_SIDE_RIGHT:
            if keys_pressed[pygame.K_UP]:
                if self.player_right.top > 0:
                    self.player_right.y -= PLAYER_SPEED
            if keys_pressed[pygame.K_DOWN]:
                if self.player_right.bottom < HEIGHT:
                    self.player_right.y += PLAYER_SPEED
            if self.ball_velocity[0] < 0:
                if self.player_left.centery > self.ball.centery:
                    self.player_left.y -= (PLAYER_SPEED - 3)
                if self.player_left.centery < self.ball.centery:
                    self.player_left.y += (PLAYER_SPEED - 3)
        
        if self.game_mode == GAME_MODE_2_PLAYERS and self.player_side == PLAYER_SIDE_BOTH:
            if keys_pressed[pygame.K_w]:
                if self.player_left.top > 0:
                    self.player_left.y -= PLAYER_SPEED
            if keys_pressed[pygame.K_s]:
                if self.player_left.bottom < HEIGHT:
                    self.player_left.y += PLAYER_SPEED
            if keys_pressed[pygame.K_UP]:
                if self.player_right.top > 0:
                    self.player_right.y -= PLAYER_SPEED
            if keys_pressed[pygame.K_DOWN]:
                if self.player_right.bottom < HEIGHT:
                    self.player_right.y += PLAYER_SPEED

    def update(self):
        if self.ball.right <= 0 or self.ball.left >= WIDTH:
            if self.ball.right <= 0:
                self.player_right_score += 1
            if self.ball.left >= WIDTH:
                self.player_left_score += 1
            if self.player_left_score == MAX_POINTS or self.player_right_score == MAX_POINTS:
                self.game_over = True
                game_over_dict = {}
                game_over_dict["left"] = "winner" if self.player_left_score == MAX_POINTS else "loser"
                game_over_dict["right"] = "winner" if self.player_right_score == MAX_POINTS else "loser"
                game_over_event = pygame.event.Event(pygame.USEREVENT, game_over_dict)
                pygame.event.post(game_over_event)
            self.ball.x = (WIDTH // 2) - (BALL_RADIUS // 2)
            self.ball.y = (HEIGHT // 2) - (BALL_RADIUS // 2)
            self.ball_velocity = [0, 0]
            self.short_break_start = pygame.time.get_ticks()
            self.short_break = True
        
        if self.short_break:
            self.short_break_stopwatch = pygame.time.get_ticks()
            if self.short_break_stopwatch - self.short_break_start >= 1000:
                self.ball_velocity = [BALL_SPEED, BALL_SPEED]
                self.ball_velocity[0] *= random.choice([1, -1])
                self.ball_velocity[1] *= random.choice([1, -1])
                self.short_break = False

        if self.ball.top <= 0:
            self.ball_velocity[1] *= -1
        if self.ball.bottom >= HEIGHT:
            self.ball_velocity[1] *= -1

        if self.ball.colliderect(self.player_left) and self.ball.left >= (self.player_left.right - (self.player_left.width // 2)):
            self.ball_velocity[0] *= -1
        if self.ball.colliderect(self.player_right) and self.ball.right <= (self.player_right.left + (self.player_right.width // 2)):
            self.ball_velocity[0] *= -1

        self.ball.x += self.ball_velocity[0]
        self.ball.y += self.ball_velocity[1]

    def render(self, screen):
        screen.fill(BLACK)

        player_left_score_render = self.font.render(str(self.player_left_score), True, WHITE)
        player_right_score_render = self.font.render(str(self.player_right_score), True, WHITE)
        screen.blit(player_left_score_render, ((WIDTH // 4) - (player_left_score_render.get_width() // 2), 50))
        screen.blit(player_right_score_render, (((3 * WIDTH) // 4) - (player_right_score_render.get_width() // 2), 50))

        if not self.game_over:
            pygame.draw.rect(screen, WHITE, self.player_left)
            pygame.draw.rect(screen, WHITE, self.player_right)
            pygame.draw.ellipse(screen, WHITE, self.ball)
        else:
            left_str = "left"
            right_str = "right"
            winner_str = left_str if self.player_left_score == MAX_POINTS else right_str
            result_str = "Player " + winner_str + " won!"
            game_result = self.font.render(result_str, True, WHITE)
            screen.blit(game_result, ((WIDTH // 2) - (game_result.get_width() // 2), (HEIGHT // 2) - (game_result.get_height() // 2)))

        pygame.display.flip()

def main():
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Pong")
    clock = pygame.time.Clock()

    current_screen = GameModeScreen()

    while True:
        next_screen = current_screen.handle_input()

        if next_screen != None:
            current_screen = next_screen

        current_screen.update()
        current_screen.render(screen)

        clock.tick(FPS)

if __name__ == "__main__":
    main()
