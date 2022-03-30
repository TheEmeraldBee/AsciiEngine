import pygame


class Time:
    def __init__(self):
        self.getTicksLastFrame: float = 0

    def deltaTime(self) -> float:
        t = pygame.time.get_ticks()
        deltaTime = (t - self.getTicksLastFrame) / 1000.0
        self.getTicksLastFrame = t
        return deltaTime
