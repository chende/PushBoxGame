
class LevelManager:
    # 关卡存放表，每一项用字符串表示关卡信息
    level_store = [
        [
            '4_3_6_6_0b1c0c1a3a1e2b1b3a4b2a1c2c1a0a1e',
            '4_3_6_6_1g2a3a2b1b3a4a2b1b2a1a4a2a1b3a4a2b1g',
            '3_2_6_6_1g2d1b2a4a2a3a1b2a1a4a3a1b2a4a2a3a1g'
        ],
        [
            '5_2_7_8_0b1e0b1a2c1d4a2b1b2c4a1c2a3a2a3a1a0a1b2a4a3a1a0b1a2c1a0b1e0a',
            '4_5_7_7_1h3a1a2c1b3a2c3a1b2c4a2a1e4b1a0c1a2b1a0c1d',
            '7_1_9_8_0c1j3a2c1b2b4c2b1b3a1b3a1b3a1b2c4a2c1b2b4a3a1a2a1f2c1a0d1e0a'
        ],
        [
            '1_3_8_7_0b1f0a1b2d1c2a4c2a1b2b4a3b2a1b2a4a3c1f2b1a0d1d0a',
            '4_6_8_8_0a1f0b1a3a2a3b1a0b1a3a2a4a3a1a0a1c2b4a1c2a4a2b4a2a1b2a1a4a1b2a1b2f1i',
            '4_4_8_7_0b1d0c1a2d1a0a1a2a4a2a4b2a1b3f1b2a4b2a4a2a1a0a1b2b1b0d1b0c'
        ]
    ]
    level_num = 0

    def __init__(self):
        self.level_num = 0

    # 加载关卡
    def load_level(self, grade_num, level_num):
        a2z = 'abcdefghijklmnopqrstuvwxyz'
        encoded = self.level_store[grade_num - 1][level_num - 1]
        read_index = 0
        player_grid_x, read_index = self.read_value(encoded, read_index)
        player_grid_y, read_index = self.read_value(encoded, read_index)
        WIDTH, read_index = self.read_value(encoded, read_index)
        HEIGHT, read_index = self.read_value(encoded, read_index)
        GRID = [[None for i in range(WIDTH)] for j in range(HEIGHT)]
        tile_index = 0
        while read_index < len(encoded):
            tile, read_index = self.read_value(encoded, read_index)
            times = a2z.find(encoded[read_index - 1]) + 1
            for i in range(times):
                tile_grid_x = tile_index % WIDTH
                tile_grid_y = tile_index // WIDTH
                GRID[tile_grid_y][tile_grid_x] = tile
                tile_index += 1
        print(GRID)
        return GRID, WIDTH, HEIGHT, player_grid_x, player_grid_y

    def read_value(self, level_string, index):
        value_str = ''
        while '0' <= level_string[index] <= '9':
            value_str += level_string[index]
            index += 1
        index += 1
        value = int(value_str)
        return value, index