import turtle

class StartPage:
    backgroundPicture = ""

    def __init__(self, backgroundPicture):
        self.backgroundPicture = backgroundPicture

    def display(self):
        self.setBackGround()

        mypen = turtle.Pen()
        mypen.hideturtle()
        mypen.speed(0)
        self.drawMoon(mypen)

        buttonStart = self.createButton("resources/start_button.gif", 300, -300)
        buttonStart.onclick(self.onButtonStartClick)

        turtle.done()

    def setBackGround(self):
        myscreen = turtle.Screen()
        myscreen.bgcolor("midnightblue")

    def drawMoon(self, pen):
        # 画笔移动
        pen.penup()
        pen.goto(-200, 200)
        pen.pendown()

        # 画月亮
        pen.pencolor("lightyellow")
        pen.dot(100)
        pen.forward(30)
        pen.pencolor("midnightblue")
        pen.dot(100)


    def createButton(delf, button_shape, x, y):
        screen = turtle.Screen()
        screen.register_shape(button_shape)
        button = turtle.Turtle()
        button.shape(button_shape)
        button.penup()
        button.goto(x, y)
        return button

    def onButtonStartClick(self, x, y):
        turtle.bye()
