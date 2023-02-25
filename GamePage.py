import turtle
from LevelManager import LevelManager

class GamePage:
    gameLevel = 0

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

    timer = 0
    counter = 0

    level_gap = False
    levelManager = None
    win_or_lose = turtle.Pen()

    def __init__(self, gameLevel):
        self.gameLevel = gameLevel

    def display(self):
        turtle.setup(800, 800)

        self.levelManager = LevelManager()
        level_store_length = len(self.levelManager.level_store)
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

        # 监听
        turtle.onkeyrelease(self.move_up, 'Up')
        turtle.onkeyrelease(self.move_down, 'Down')
        turtle.onkeyrelease(self.move_left, 'Left')
        turtle.onkeyrelease(self.move_right, 'Right')
        turtle.onkeyrelease(self.load_level, 'r')
        turtle.listen()

        self.create_button(skindir + 'player.gif', -300, -350).onclick(self.button_left_click)
        self.create_button(skindir + 'player.gif', -160, -350).onclick(self.button_right_click)
        self.create_button(skindir + 'player.gif', -230, -280).onclick(self.button_up_click)
        self.create_button(skindir + 'player.gif', -230, -350).onclick(self.button_down_click)
        self.create_button(skindir + 'player.gif', 100, -350).onclick(self.button_return_click)

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
                turtle.goto(-100, 300)
                turtle.write("计时: " + str(self.timer) + "       计步：" + str(self.counter), align="left", font=("Arial", 24, "normal"))

                # 胜负判断
                win_flag = True
                for i in self.GRID:
                    if 3 in i:
                        win_flag = False
                        break

            if win_flag and not self.level_gap:
                self.level_gap = True
                if self.level_num < level_store_length:
                    self.win_or_lose.shape(skindir + 'success.gif')
                    self.win_or_lose.onclick(self.next_level)
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

    def load_level(self):
        self.GRID, self.WIDTH, self.HEIGHT, self.player_grid_x, self.player_grid_y = self.levelManager.load_level(self.level_num)
        self.timer = 0
        self.counter = 0

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