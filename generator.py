import algo
import random
import pandas as pd
import numpy as np


'''
data = pd.read_csv('sudoku.csv')
data = pd.DataFrame({'Quizzes' : data['quizzes'], 'Solutions' : data['solutions']})
data.drop(['Solutions'], axis = 1)
data.head(5000).to_csv('mysudoku.csv')
'''

def load():
    data = pd.read_csv('mysudoku.csv')
    data = pd.DataFrame({'Quizzes' : data['Quizzes']})

    return data

def getBoard(show=False):
    data = load()
    r = random.randint(0, 4999)
    q = list(map(int, str(data.iloc[r][0])))
    q = np.reshape(q, (9, 9)).tolist()

    if show:
        algo.showBoard(q)

    return q


if __name__ == '__main__':
    print(getBoard(True))

