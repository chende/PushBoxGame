import pandas as pd
import XPath as xp

class Ranking:
    data_path = ''
    userName = "小宇"
    df = pd.DataFrame(columns=['玩家','等级','关卡','积分'])

    def __init__(self):
        self.data_path = xp.instance.get_data_path()
        try:
            self.df = pd.read_csv(self.data_path)
            # data = {'玩家': ['峻宇','乐乐'], '等级': [2,2], '关卡': [3,2], '积分': [30,26]}
            # self.df = pd.DataFrame(data, columns=['玩家','等级','关卡','积分'])
        except Exception as e:
            print("读取文件失败" + str(e))

    def addRecord(self, grade_num, level_num, score):
        # self.data.append([self.userName, grade_num, level_num, score])
        new_data = {'玩家': self.userName, '等级': grade_num, '关卡': level_num, '积分': score}
        df1 = self.df.append(new_data, ignore_index=True)

        df2 = df1.sort_values(['积分', '等级', '关卡', '玩家'], ascending=[False, False, False, True])
        self.df = df2.drop_duplicates(subset=['玩家'], keep='first')

        try:
            self.df.to_csv(self.data_path, index=False)
        except Exception as e:
            print("写取文件失败" + str(e))

        print(self.df)

    def showRankingStr(self):
        str = ''
        if not self.df.empty:
            df2 = self.df.copy(deep=True)
            df2['等级'] = df2['等级'].apply(self.toGradeStr)
            df2['关卡'] = df2['关卡'].apply(self.toLevelStr)
            str = df2.to_string(header=False, index=False, max_rows=8)
        return str

    def deleteRanking(self, userName):
        self.df = self.df.drop(self.df[self.df['玩家'] == userName].index)
        self.df.to_csv(self.data_path, index=False)
        print(self.df)

    def toGradeStr(self, grade_num):
        if grade_num == 1:
            return "初级"
        elif grade_num == 2:
            return "中级"
        else:
            return "高级"

    def toLevelStr(self, level_num):
        if level_num == 1:
            return "第一关"
        elif level_num == 2:
            return "第二关"
        else:
            return "第三关"


# 单例对象
instance = Ranking()