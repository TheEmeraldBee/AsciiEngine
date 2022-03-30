import asciiEngine


class Game:
    def __init__(self):
        self.window = asciiEngine.Window("MyGame", (720, 480))
        self.running = True
        self.timeHandler = asciiEngine.Time()

    def Run(self):
        self.window.draw((("A" * 180) + "\n") * 30, (255, 255, 255), (10, 10))
        self.window.createWindow()

        while self.running:
            deltaTime = self.timeHandler.deltaTime()

            if self.window.shouldQuit():
                self.running = False

            self.window.updateWindow()


if __name__ == '__main__':
    game = Game()
    game.Run()