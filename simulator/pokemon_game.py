import pygame


pygame.init()


scizor = pygame.image.load("sprites/scizor.gif")


class PokemonSprite(pygame.sprite.Sprite):
    def __init__(self):
        # Call the parent class (Sprite) constructor
        super().__init__()
        
        # Set the image for the sprite
        self.image = scizor
        
        # Create a rectangle object from the image's dimensions
        self.rect = self.image.get_rect()
        
        # Set initial position (e.g., top-left corner)
        self.rect.x = 0
        self.rect.y = 0

    def update(self):
        # Add logic here to update the sprite's position or state each frame
        pass

scizor_sprite = PokemonSprite()

all_sprites = pygame.sprite.Group()
all_sprites.add(scizor_sprite)

screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
clock = pygame.time.Clock()
running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Update all sprites
    all_sprites.update()

    # Clear the screen (fill with white, for example)
    screen.fill((255, 255, 255))

    # Draw all sprites onto the screen
    all_sprites.draw(screen)

    # Flip the display to show the new frame
    pygame.display.flip()

    # Cap the frame rate
    clock.tick(60)

pygame.quit()