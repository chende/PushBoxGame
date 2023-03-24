import pandas as pd
import math

class Score:
    # data = [[1,1,2,6],[2,1,36,63],[1,2,6,13],[1,3,12,16],[2,1,22,44]]
    data = []

    def __init__(self):
        pass

    def addRecord(self, grade_num, level_num, time_taken, step_count):
        self.data.append([grade_num, level_num, time_taken, step_count])

    def caculateScore(self):
        df = pd.DataFrame(self.data, columns=['等级', '关卡', '时间', '步数'])
        df2 = df.sort_values(['等级', '关卡','时间', '步数'], ascending=[True, True, True, True])
        df3 = df2.drop_duplicates(subset=['等级', '关卡'], keep='first')

        score = 0
        for index, row in df3.iterrows():
            score = score + (row['等级'])*10 - math.floor(math.log((row['时间']+1),2)) - math.floor(math.log(row['步数'],2))

        # print("score:" + str(score))
        return score

# 单例对象
instance = Score()