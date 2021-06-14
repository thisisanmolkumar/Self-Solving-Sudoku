import algo
import random
import pandas as pd
import numpy as np


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
