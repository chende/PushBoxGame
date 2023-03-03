# import StartPage
from StartPage import StartPage
from GamePage import GamePage
from XPath import XPath

if __name__ == '__main__':
    resrouce_path = XPath.get_resource_path("resources")

    startPage = StartPage(resrouce_path)
    startPage.display()

    gamePage = GamePage(resrouce_path, startPage.gradeNum)
    gamePage.display()
