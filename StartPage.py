import turtle

class StartPage:
    backgroundPicture = ""
    alive = True

    def __init__(self, backgroundPicture):
        self.backgroundPicture = backgroundPicture

    def display(self):
        myscreen = turtle.Screen()
        turtle.tracer(False)
        myscreen.bgpic("resources/background.gif")

        buttonStart = self.createButton("resources/start_button.gif", 200, -300)
        buttonStart.onclick(self.onButtonStartClick)

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
