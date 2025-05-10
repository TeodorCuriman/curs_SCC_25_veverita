import pygame
import sys

class Animal:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((800, 600))
        pygame.display.set_caption("Veverița care chicotește")
        
        self.clock = pygame.time.Clock()
        self.image = pygame.image.load("veverita.png")
        self.sound = pygame.mixer.Sound("veverita.wav")
        
        self.x = 100
        self.y = 300
        self.speed = 5

    def run(self):
        running = True
        while running:
            self.screen.fill((255, 255, 255))  # alb
            
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        self.sound.play()

            keys = pygame.key.get_pressed()
            if keys[pygame.K_LEFT]:
                self.x -= self.speed
            if keys[pygame.K_RIGHT]:
                self.x += self.speed

            self.screen.blit(self.image, (self.x, self.y))

            font = pygame.font.SysFont(None, 48)
            text = font.render("Veverița", True, (0, 0, 0))
            self.screen.blit(text, (10, 10))

            pygame.display.flip()
            self.clock.tick(60)

        pygame.quit()
        sys.exit()

if __name__ == "__main__":
    animal = Animal()
    animal.run()
