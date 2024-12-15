import pygame
import random

# Initialize Pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 800, 600
FPS = 60
PLAYER_VEL = 5
GRAVITY = 1
SCROLL_SPEED = 3  # Background scroll speed
OBSTACLE_GAP = 300  # Distance between obstacles (increase gap for more space)

# Colors
WHITE = (255, 255, 255)
RED = (255, 0, 0)

# Screen setup
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Sonic Game")

# Load Sonic and Background images
sonic_img_path = "C:\\Users\\Dell\\Downloads\\image-removebg-preview.png"  # Update this path with your Sonic image
background_img_path = "C:\\Users\\Dell\\Downloads\\sonic bg.png"  # Update this path with your new Sonic background

player_img = pygame.image.load(sonic_img_path)
player_img = pygame.transform.scale(player_img, (50, 50))  # Resize the image if necessary
background_img = pygame.image.load(background_img_path)
background_img = pygame.transform.scale(background_img, (WIDTH, HEIGHT))  # Scale background to fit screen

# Player class
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = player_img
        self.rect = self.image.get_rect()
        self.x_vel = 0
        self.y_vel = 0
        self.on_ground = False
        self.jump_count = 0
        self.score = 0

    def update(self):
        self.x_vel = 0
        keys = pygame.key.get_pressed()

        # Horizontal Movement
        if keys[pygame.K_LEFT]:
            self.x_vel = -PLAYER_VEL
        if keys[pygame.K_RIGHT]:
            self.x_vel = PLAYER_VEL

        # Gravity
        if not self.on_ground:
            self.y_vel += GRAVITY
        else:
            self.y_vel = 0
            self.jump_count = 0

        # Jumping
        if keys[pygame.K_SPACE] and self.jump_count < 2:  # Double jump
            self.y_vel = -15
            self.jump_count += 1
        
        # Update the position
        self.rect.x += self.x_vel
        self.rect.y += self.y_vel

        # Collision with the ground
        if self.rect.bottom > HEIGHT - 50:
            self.rect.bottom = HEIGHT - 50
            self.on_ground = True
        else:
            self.on_ground = False

        # Collision with the walls (left and right boundaries)
        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.right > WIDTH:
            self.rect.right = WIDTH

# Obstacle class
class Obstacle(pygame.sprite.Sprite):
    def __init__(self, x, y, width, height):
        super().__init__()
        self.image = pygame.Surface((width, height))
        self.image.fill(RED)  # Red color for the obstacle
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.speed = random.randint(2, 5)

    def update(self):
        # Move the obstacle from right to left
        self.rect.x -= self.speed

        # If the obstacle moves off the screen, reset it to the right side
        if self.rect.right < 0:
            self.rect.left = WIDTH
            self.rect.y = HEIGHT - 100  # Adjust obstacle position vertically

# Ground class
class Ground(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((WIDTH, 50))
        self.image.fill((0, 255, 0))  # Green color for the ground
        self.rect = self.image.get_rect()
        self.rect.x = 0
        self.rect.y = HEIGHT - 50

# Score function
def draw_score(score, high_score):
    font = pygame.font.Font(None, 36)
    score_text = font.render(f"Score: {score}", True, (255, 255, 255))
    high_score_text = font.render(f"High Score: {high_score}", True, (255, 255, 255))
    screen.blit(score_text, (10, 10))
    screen.blit(high_score_text, (WIDTH - 200, 10))

# Game loop
def main():
    clock = pygame.time.Clock()

    # Create the player object
    player = Player()

    # Create the ground
    ground = Ground()

    # Create sprite groups
    all_sprites = pygame.sprite.Group()
    obstacles = pygame.sprite.Group()
    all_sprites.add(player, ground)

    # Create fewer obstacles (less obstacles)
    for i in range(1, 3):  # Create only 3 obstacles spaced out
        x_pos = i * OBSTACLE_GAP + WIDTH  # Start from right and space obstacles
        obstacle = Obstacle(x_pos, HEIGHT - 100, 50, 50)  # Obstacle size and position
        obstacles.add(obstacle)
        all_sprites.add(obstacle)

    # Game variables
    high_score = 0
    background_x = 0  # Position for the scrolling background
    running = True
    while running:
        clock.tick(FPS)

        # Event handling
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        
        # Update all sprites
        all_sprites.update()

        # Check for collisions between the player and obstacles
        if pygame.sprite.spritecollide(player, obstacles, False):
            if player.score > high_score:
                high_score = player.score
            print("Game Over!")
            player.score = 0  # Reset score after game over
            player.rect.x = 100  # Reset player position
            player.rect.y = HEIGHT - 100  # Reset player vertical position
            player.jump_count = 0  # Reset jump count

            # Show restart option
            font = pygame.font.Font(None, 48)
            restart_text = font.render("Press 'R' to Restart", True, (255, 255, 255))
            screen.blit(restart_text, (WIDTH // 3, HEIGHT // 2))
            pygame.display.flip()

            waiting_for_restart = True
            while waiting_for_restart:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        running = False
                        waiting_for_restart = False
                    if event.type == pygame.KEYDOWN and event.key == pygame.K_r:
                        main()  # Restart the game

            break  # End the current game loop

        # Scrolling the background
        background_x -= SCROLL_SPEED
        if background_x <= -WIDTH:
            background_x = 0

        # Update score
        player.score += 1  # Increment the score every frame (for example, increase it for each second of playtime)

        # Draw everything
        screen.fill(WHITE)  # Fill the screen with white before drawing the background
        screen.blit(background_img, (background_x, 0))  # Draw the background image
        screen.blit(background_img, (background_x + WIDTH, 0))  # Draw second part of the background for looping

        all_sprites.draw(screen)

        # Draw the score and high score
        draw_score(player.score, high_score)

        pygame.display.flip()

    pygame.quit()

# Start the game
if __name__ == "__main__":
    main()
