import turtle

class StartPage:
    gradeNum = 1
    alive = True
    instructionPage = None

    def __init__(self):
        self.gradeNum = 1

    def display(self):
        turtle.setup(800, 860)
        myscreen = turtle.Screen()
        turtle.tracer(False)
        myscreen.bgcolor("#E0FFFF")
        myscreen.bgpic("resources/start/back_ground.png")

        buttonStart = self.createButton("resources/start/start_button.gif", 0, -125)
        buttonStart.onclick(self.onButtonStartClick)

        buttonEasy = self.createButton("resources/start/easy_button.gif", 320, 0)
        buttonEasy.onclick(self.onButtonEasyClick)
        buttonMedium = self.createButton("resources/start/medium_button.gif", 320, -80)
        buttonMedium.onclick(self.onButtonMediumClick)
        buttonDifficult = self.createButton("resources/start/difficult_button.gif", 320, -160)
        buttonDifficult.onclick(self.onButtonDifficultClick)

        buttonInstruction = self.createButton("resources/start/instruction_button.gif", 320, -380)
        buttonInstruction.onclick(self.onButtonInstructionClick)

        while self.alive:
            turtle.update()

        buttonStart.hideturtle()
        myscreen.clearscreen()

    def createButton(self, button_shape, x, y):
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

    def onButtonEasyClick(self, x, y):
        turtle.hideturtle()
        self.alive = False
        self.gradeNum = 0

    def onButtonMediumClick(self, x, y):
        turtle.hideturtle()
        self.alive = False
        self.gradeNum = 1

    def onButtonDifficultClick(self, x, y):
        turtle.hideturtle()
        self.alive = False
        self.gradeNum = 2

    def onButtonInstructionClick(self, x, y):
        self.instructionPage = turtle.Pen()
        self.instructionPage.shape('resources/start/instruction_words.gif')
        self.instructionPage.onclick(self.closeInstructions)

    def closeInstructions(self, x, y):
        self.instructionPage.hideturtle()