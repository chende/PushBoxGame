import turtle
from LevelManager import LevelManager
import copy
import time

class GamePage:
    grade_num = 1

    # 关卡初始化
    SIZE = 70
    movement_grid_x = 0
    movement_grid_y = 0

    level_num = 1
    level_num_pre = 1

    WIDTH = 0
    HEIGHT = 0
    GRID = []
    player_grid_x = 0
    player_grid_y = 0

    GRID_pre = []
    player_grid_x_pre = 0
    player_grid_y_pre = 0
    can_step_back = False

    timer = 0
    counter = 0

    level_gap = False
    levelManager = None
    win_or_lose = None

    def __init__(self, grade_num):
        self.grade_num = grade_num

    def display(self):

        self.levelManager = LevelManager()
        grade_length = len(self.levelManager.level_store)
        level_store_length = len(self.levelManager.level_store[self.grade_num])
        self.load_level()

        # 左上角砖块中心坐标
        origin_x = 0 - self.SIZE * (self.WIDTH / 2 - 0.5)
        origin_y = 0 + self.SIZE * (self.HEIGHT / 2 - 0.5)

        # 添加素材
        skindir = 'resources/skin1/'
        tile_shapes = [skindir + 'empty.gif', skindir + 'wall.gif', skindir + 'road.gif', skindir + 'target.gif', skindir + 'box.gif', skindir + 'target_box.gif']
        for i in tile_shapes:
            turtle.addshape(i)
        turtle.addshape(skindir + 'player.gif')
        turtle.addshape(skindir + 'success.gif')
        turtle.addshape(skindir + 'pass.gif')

        # 初始化砖块和玩家画笔
        tile = turtle.Pen()
        tile.penup()
        player = turtle.Pen()
        player.shape(skindir + 'player.gif')
        player.penup()

        turtle.tracer(False)

        myscreen = turtle.Screen()
        myscreen.bgcolor("#E0FFFF")
        # 监听
        turtle.onkeyrelease(self.move_up, 'Up')
        turtle.onkeyrelease(self.move_down, 'Down')
        turtle.onkeyrelease(self.move_left, 'Left')
        turtle.onkeyrelease(self.move_right, 'Right')
        turtle.onkeyrelease(self.load_level, 'r')
        turtle.listen()

        buttondir = 'resources/button/'
        self.create_button(buttondir + 'left.gif', -320, -380).onclick(self.button_left_click)
        self.create_button(buttondir + 'right.gif', -180, -380).onclick(self.button_right_click)
        self.create_button(buttondir + 'up.gif', -250, -310).onclick(self.button_up_click)
        self.create_button(buttondir + 'down.gif', -250, -380).onclick(self.button_down_click)
        self.create_button(buttondir + 'back.gif', 100, -380).onclick(self.button_step_back_click)
        self.create_button(buttondir + 'return.gif', 200, -380).onclick(self.button_return_click)

        turtle.hideturtle()
        turtle.ontimer(self.count_up, 1000)

        while True:
            # 读取下一关卡
            if self.level_num != self.level_num_pre:
                self.load_level()
                # 左上角砖块中心坐标
                origin_x = 0 - self.SIZE * (self.WIDTH / 2 - 0.5)
                origin_y = 0 + self.SIZE * (self.HEIGHT / 2 - 0.5)
                self.level_num_pre = self.level_num

            if not self.level_gap:
                # 清空地图
                tile.clear()
                player.clear()
                # 计算移动量
                player_temp_grid_x = self.player_grid_x
                player_temp_grid_y = self.player_grid_y
                self.player_grid_x += self.movement_grid_x
                self.player_grid_y += self.movement_grid_y
                if self.is_wall(self.player_grid_x, self.player_grid_y, self.GRID):
                    self.player_grid_x -= self.movement_grid_x
                    self.player_grid_y -= self.movement_grid_y
                elif self.is_box(self.player_grid_x, self.player_grid_y, self.GRID):
                    box_next_x = self.player_grid_x + self.movement_grid_x
                    box_next_y = self.player_grid_y + self.movement_grid_y
                    if self.is_box(box_next_x, box_next_y, self.GRID) or self.is_wall(box_next_x, box_next_y, self.GRID):
                        self.player_grid_x -= self.movement_grid_x
                        self.player_grid_y -= self.movement_grid_y
                    else:
                        # 记录上次的地图和player位置
                        self.GRID_pre = copy.deepcopy(self.GRID)
                        self.player_grid_x_pre = player_temp_grid_x
                        self.player_grid_y_pre = player_temp_grid_y
                        self.can_step_back = True

                        self.GRID[box_next_y][box_next_x] += 2
                        self.GRID[self.player_grid_y][self.player_grid_x] -= 2
                if player_temp_grid_x != self.player_grid_x:
                    self.counter += 1
                if player_temp_grid_y != self.player_grid_y:
                    self.counter += 1

                self.movement_grid_x = 0
                self.movement_grid_y = 0

                # 刷新地图
                for i in range(len(self.GRID)):
                    for j in range(len(self.GRID[i])):
                        tile.shape(tile_shapes[self.GRID[i][j]])
                        tile.goto(origin_x + j * self.SIZE, origin_y - i * self.SIZE)
                        tile.stamp()

                # 刷新player
                player.goto(origin_x + self.player_grid_x * self.SIZE, origin_y - self.player_grid_y * self.SIZE)
                player.stamp()

                # 刷新计时器和计步器
                turtle.clear()
                turtle.goto(-100, 350)
                turtle.pencolor("red")
                turtle.write("计时: " + str(self.timer) + "       计步：" + str(self.counter), align="left", font=("Arial", 36, "normal"))

                # 胜负判断
                win_flag = True
                for i in self.GRID:
                    if 3 in i:
                        win_flag = False
                        break

            if win_flag and not self.level_gap:
                self.win_or_lose = turtle.Pen()
                self.level_gap = True
                if self.level_num < level_store_length:
                    self.win_or_lose.shape(skindir + 'success.gif')
                    self.win_or_lose.onclick(self.next_level)
                elif self.grade_num < grade_length:
                    self.win_or_lose.shape(skindir + 'pass.gif')
                    self.win_or_lose.onclick(self.next_grade)
                else:
                    self.win_or_lose.shape(skindir + 'pass.gif')

            turtle.update()

        turtle.done

    def move_up(self):
        self.movement_grid_y = -1

    def move_down(self):
        self.movement_grid_y = 1

    def move_left(self):
        self.movement_grid_x = -1

    def move_right(self):
        self.movement_grid_x = 1

    def next_level(self, x, y):
        self.level_num += 1
        self.win_or_lose.hideturtle()
        self.level_gap = False
        self.can_step_back = False

    def next_grade(self, x, y):
        self.grade_num += 1
        self.level_num = 1
        self.win_or_lose.hideturtle()
        self.level_gap = False
        self.can_step_back = False

    def load_level(self):
        self.GRID, self.WIDTH, self.HEIGHT, self.player_grid_x, self.player_grid_y = self.levelManager.load_level(self.grade_num, self.level_num)
        self.timer = 0
        self.counter = 0
        self.can_step_back = False

    def is_wall(self, grid_x, grid_y, grid):
        return grid[grid_y][grid_x] == 1

    def is_box(self, grid_x, grid_y, grid):
        return grid[grid_y][grid_x] == 4 or grid[grid_y][grid_x] == 5

    def button_left_click(self, x, y):
        self.move_left()

    def button_right_click(self, x, y):
        self.move_right()

    def button_up_click(self, x, y):
        self.move_up()

    def button_down_click(self, x, y):
        self.move_down()

    def button_return_click(self, x, y):
        self.load_level()

    def button_step_back_click(self, x, y):
        if self.can_step_back == True:
            self.GRID = copy.deepcopy(self.GRID_pre)
            self.player_grid_x = self.player_grid_x_pre
            self.player_grid_y = self.player_grid_y_pre
            self.can_step_back = False
        else:
            pen = turtle.Pen()
            pen.color("red")
            pen.write("不能返回上一步", align="left", font=("Arial", 36, "normal"))
            time.sleep(1)
            pen.clear()

    def create_button(self, button_shape, x, y):
        screen = turtle.Screen()
        screen.register_shape(button_shape)
        button = turtle.Turtle()
        button.shape(button_shape)
        button.penup()
        button.goto(x, y)
        return button

    def count_up(self):
        self.timer += 1
        turtle.ontimer(self.count_up, 1000)