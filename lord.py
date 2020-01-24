# lords have
# two quest types or building
# amount of vp awarded

from quest import Quest
import random
import pandas as pd

typeslist = ['Building', 'Commerce', 'Skullduggery', 'Warfare', 'Piety', 'Arcana']
names = []

class Lord: 
    def __init__(self, types, name):
        self.name = name
        self.types = types
        if self.types == ['Building']:
            self.points = 6
        else:
            self.points = 4

    def __repr__(self):
        questtypes = ''
        if self.types == ['Building']:
            questtypes = 'Buildings'
        else:
            questtypes = str(self.types[0]) + ' and ' + str(self.types[1])
        return 'this lord has: ' + questtypes + ' for ' + str(self.points) + ' points each\n'
    
    def award(self, quests):        
        return sum(q.questtype in self.types for q in quests) * self.points

class Deck():
    def __init__(self):
        lord_df = pd.read_csv('lords.csv')
        lord_df.set_index('name', inplace=True)
        self.lords = {}
        self.cards = []
        for name in lord_df.index:
            types = [lord_df.loc[name,'type1'],lord_df.loc[name,'type2']]
            self.lords[name] = Lord(types,name)
            self.cards.append(name)

    def shuffle(self, times = 1):
        for i in range(times):
            random.shuffle(self.cards)

    def draw(self):
        return self.cards.pop()