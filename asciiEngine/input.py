import pygame


class InputManager:
    def __init__(self):
        self.lastKeysDown = pygame.key.get_pressed()

        self.keysDown = pygame.key.get_pressed()

    def getKeyPressing(self, key) -> bool:
        return self.keysDown[key]

    def getKeyDown(self, key) -> bool:
        if self.keysDown[key] and not self.lastKeysDown[key]:
            return True
        return False

    def getKeyUp(self, key) -> bool:
        if not self.keysDown[key] and self.lastKeysDown[key]:
            return True
        return False

    def updateInput(self):
        self.lastKeysDown = self.keysDown
        self.keysDown = pygame.key.get_pressed()
