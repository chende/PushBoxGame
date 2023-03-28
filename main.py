from StartPage import StartPage
from GamePage import GamePage

if __name__ == '__main__':
    while True:
        startPage = StartPage()
        startPage.display()

        gamePage = GamePage(startPage.gradeNum)
        gamePage.display()
