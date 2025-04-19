from circleshape import *
from constants import COLOR_WHITE

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def update(self, delta_time):
        self.position += self.velocity * delta_time

    def draw(self, screen):
        pygame.draw.circle(screen, COLOR_WHITE, self.position, self.radius, 2)