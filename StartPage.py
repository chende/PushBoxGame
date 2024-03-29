import turtle

import XPath as xp
import ranking as rk
import scoring as sc

class StartPage:
    resrouce_path = ''
    gradeNum = 1
    alive = True
    instructionPage = None
    showInstruction = False
    rankingText = None
    userName = ""
    fontSize=30

    def __init__(self):
        self.resrouce_path = xp.instance.get_resource_path()
        self.gradeNum = 1
        self.userName = rk.instance.userName

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
        turtle.addshape(start_path + "ranking.gif")

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

        buttonLogin = self.createButton(start_path + "button_login.gif", -320, 0)
        buttonLogin.onclick(self.onButtonLoginClick)
        buttonRanking = self.createButton(start_path + "button_ranking.gif", -320, -80)
        buttonRanking.onclick(self.onButtonRankingClick)
        buttonRemoveScore = self.createButton(start_path + "button_remove_score.gif", -320, -160)
        buttonRemoveScore.onclick(self.onButtonRemoveScoreClick)

        while self.alive:
            turtle.clear()
            turtle.penup()
            turtle.goto(-400, 100)
            turtle.pencolor("red")
            turtle.hideturtle()
            turtle.write("玩家: " + str(self.userName), align="left", font=("Arial", self.fontSize, "normal"))
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
        self.rankingText.clear()

    def onButtonLoginClick(self, x, y):
        input = turtle.textinput("玩家登陆", "请输入姓名：")
        if input != None and input != '':
            rk.instance.userName = self.userName = input
            sc.instance.clearScore()

    def onButtonRankingClick(self, x, y):
        if self.showInstruction == False:
            self.instructionPage = turtle.Pen()
            self.instructionPage.shape(self.resrouce_path + '/' + 'ranking.gif')
            self.instructionPage.onclick(self.closeInstructions)
            self.showInstruction = True

            str = rk.instance.showRankingStr()
            line_count = str.count('\n') + 1
            self.rankingText = turtle.Pen()
            self.rankingText.penup()
            self.rankingText.pencolor("red")
            self.rankingText.goto(0, 30)
            self.rankingText.write('玩家  等级  关卡  积分', align="center", font=("Arial", self.fontSize, "bold"))
            self.rankingText.pencolor("orange")
            self.rankingText.goto(0, -line_count*self.fontSize)
            self.rankingText.write(str, align="center", font=("Arial", self.fontSize, "normal"))
            self.rankingText.hideturtle()

    def onButtonRemoveScoreClick(self, x, y):
        input = turtle.textinput("删除玩家积分", "请输入要删除积分的玩家姓名：")
        if input != None and input != '':
            rk.instance.deleteRanking(input)
            if input == self.userName:
                sc.instance.clearScore()