from circleshape import *
from constants import PLAYER_SHOT_RADIUS, PLAYER_SHOT_SPEED, COLOR_WHITE

class PlayerShot(CircleShape):
    def __init__(self, x, y):
        super().__init__(x, y, PLAYER_SHOT_RADIUS)

    def update(self, delta_time):
        self.position += self.velocity * delta_time

    def draw(self, screen):
        pygame.draw.circle(screen, COLOR_WHITE, self.position, self.radius, 2)