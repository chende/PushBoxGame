import turtle

class StartPage:
    backgroundPicture = ""
    alive = True

    def __init__(self, backgroundPicture):
        self.backgroundPicture = backgroundPicture

    def display(self):
        turtle.setup(800, 860)
        myscreen = turtle.Screen()
        turtle.tracer(False)
        myscreen.bgcolor("#E0FFFF")
        myscreen.bgpic("resources/back_ground.png")
        # myscreen.onclick(self.onButtonStartClick)

        buttonStart = self.createButton("resources/start_button.gif", 0, -125)
        buttonStart.onclick(self.onButtonStartClick)

        buttonStart = self.createButton("resources/easy.gif", 320, 0)
        buttonStart.onclick(self.onButtonStartClick)
        buttonStart = self.createButton("resources/medium.gif", 320, -80)
        buttonStart.onclick(self.onButtonStartClick)
        buttonStart = self.createButton("resources/difficult.gif", 320, -160)
        buttonStart.onclick(self.onButtonStartClick)

        buttonStart = self.createButton("resources/instruction.gif", 320, -400)
        buttonStart.onclick(self.onButtonInstructionClick)

        while self.alive:
            turtle.update()

        buttonStart.hideturtle()
        myscreen.clearscreen()

    def createButton(delf, button_shape, x, y):
        screen = turtle.Screen()
        screen.register_shape(button_shape)
        button = turtle.Turtle()
        button.shape(button_shape)
        button.penup()
        button.goto(x, y)
        return button

    def onButtonStartClick(self, x, y):
        turtle.hideturtle()
        self.alive = False

    def onButtonInstructionClick(self, x, y):
        turtle.hideturtle()
