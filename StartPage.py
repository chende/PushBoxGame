import turtle

class StartPage:
    resrouce_path = ''
    gradeNum = 1
    alive = True
    instructionPage = None
    showInstruction = False

    def __init__(self, resrouce_path):
        self.resrouce_path = resrouce_path
        self.gradeNum = 1

    def display(self):
        turtle.title("疯狂推箱子")
        turtle.setup(800, 860)
        turtle.screensize(700, 800)
        myscreen = turtle.Screen()
        turtle.tracer(False)
        myscreen.bgcolor("#E0FFFF")
        start_path = self.resrouce_path + "/"
        myscreen.bgpic(start_path + "back_ground.png")
        turtle.addshape(start_path + "game_guide.gif")

        buttonStart = self.createButton(start_path + "start_button.gif", 0, -125)
        buttonStart.onclick(self.onButtonStartClick)

        buttonEasy = self.createButton(start_path + "button_junior.gif", 320, 0)
        buttonEasy.onclick(self.onButtonEasyClick)
        buttonMedium = self.createButton(start_path + "button_middle.gif", 320, -80)
        buttonMedium.onclick(self.onButtonMediumClick)
        buttonDifficult = self.createButton(start_path + "button_senior.gif", 320, -160)
        buttonDifficult.onclick(self.onButtonDifficultClick)

        buttonInstruction = self.createButton(start_path + "button_instruction.gif", 320, -350)
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
        self.gradeNum = 1

    def onButtonMediumClick(self, x, y):
        turtle.hideturtle()
        self.alive = False
        self.gradeNum = 2

    def onButtonDifficultClick(self, x, y):
        turtle.hideturtle()
        self.alive = False
        self.gradeNum = 3

    def onButtonInstructionClick(self, x, y):
        if self.showInstruction == False:
            self.instructionPage = turtle.Pen()
            self.instructionPage.shape(self.resrouce_path + '/' + 'game_guide.gif')
            self.instructionPage.onclick(self.closeInstructions)
            self.showInstruction = True

    def closeInstructions(self, x, y):
        self.instructionPage.hideturtle()
        self.showInstruction = False