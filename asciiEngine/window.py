import asciiEngine
from asciiEngine.input import *


class Window:
    def __init__(self, name: str, screenSize: (int, int), bg_color: (float, float, float) = (0, 0, 0)):
        pygame.init()

        if not pygame.get_init():
            print("PyGame failed to initialize!")

        print(f"You are using AsciiEngine version: {asciiEngine.VERSION}")

        self.name = name
        self.window = None
        self.bg_color = bg_color
        self.screenSize = screenSize
        self.display = pygame.Surface(screenSize)

        self.gameFont = pygame.font.Font(None, 24)
        self.texts = {(255, 255, 255): ["GameText: Black"]}

        self.inputManager = InputManager()

        self.textSize = self.gameFont.size(" ")

        self.maxWidth = round(self.screenSize[0] / self.textSize[0])
        self.maxHeight = round(self.screenSize[1] / self.textSize[1])

    def createWindow(self):
        self.window = pygame.display.set_mode(self.screenSize, pygame.RESIZABLE)
        pygame.display.set_caption(self.name)

    def draw(self, text: str, color: (float, float, float), position: (int, int)):
        self.texts[color] = text.split("\n")

    def updateWindow(self):
        
        self.window.fill(self.bg_color)
        self.display.fill(self.bg_color)
        for color in self.texts.keys():
            img = []
            for i in range(0, len(self.texts[color])):
                img += [self.gameFont.render(self.texts[color][i], True, color)]
            for i in range(0, len(img)):
                self.display.blit(img[i], (0, i * self.textSize[1]))

        self.inputManager.updateInput()
        self.window.blit(pygame.transform.scale(self.display, self.window.get_rect().size), (0, 0))
        pygame.display.update()

    def shouldQuit(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return True
