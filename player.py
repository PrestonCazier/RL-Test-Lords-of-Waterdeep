from resourcevector import RVector
import sys
from quest import Quest
import random
import lord

numagents = [None,4,3,2,2]
names = {'yellow':'Knights of the Shield', 'grey':'City Guard', 'blue':'Silverstars', 'green':'Harpers', 'red':'Red Sashes'}


# complete order
# add draw function to main game loop after each action to reduce player resource pool and add cards to player's lists
# move onto intrigue cards

def formatOpen(quests):
    ret = ''
    if len(quests) == 0:
        return 'No open quests\n'
    for q in quests:
        if q.questtype == 'MANDATORY':
            ret += str(q) + '\n'
    for q in quests:
        if (q.questtype != 'MANDATORY') and q.plotquest:
            ret += str(q) + '\n'
    for q in quests:
        if (q.questtype != 'MANDATORY') and not q.plotquest:
            ret += str(q) + '\n'
    return ret

def formatPlot(completed):
    ret = ''
    plot = [q for q in completed if q.plotquest]
    if len(plot) == 0:
        return 'No completed plot quests\n'
    for q in plot:
        ret += str(q) + '\n'
    return ret

def formatClosed(completed):
    ret = ''
    if len([q for q in completed if not q.plotquest]) == 0:
        return 'No completed non-plot quests\n'
    for q in completed:
        if not q.plotquest:
            ret += str(q) + '\n'
    return ret

class Player:

    def __init__(self, color, totalagents):
        self.lord = None
        self.quests = []
        self.completed = []
        self.intrigues = []
        self.buildings = []
        self.name = names[color]
        self.color = color
        self.resources = RVector(0,0,0,0,0,0,0,0,0)
        self.fp = False
        self.haslieutenant = False
        self.hasambassador = False
        self.numagents = totalagents
        self.totalagents = totalagents
        return

    def __str__(self):
        color  = self.color + ' player has the folowwing resources\n' + str(self.resources) + '\n'
        agents = str(self.numagents) + ' AGENTS left to be played this round'
        if self.haslieutenant:
            agents += ' and has the lieutenant'
        if self.hasambassador:
            agents += ' and has the ambassador'
        intrigues = '\nhas {} INTRIGUE cards in hand\n'.format(len(self.intrigues))
        openquests = 'has the following open quests:\n' + formatOpen(self.quests)
        plotquests = 'has the following completed plot quests:\n' + formatPlot(self.completed)
        closedquests = 'has the following closed quests:\n' + formatClosed(self.completed)
        return color+agents+intrigues+openquests+plotquests+closedquests

    def assignLord(self, lord):
        self.lord = lord

    def gainLieutenant(self):
        self.haslieutenant = True
        return

    def setAmbassador(self, value):
        self.hasambassador = value
        return

    def gainIntrigue(self, cards):
        self.intrigues.extend(cards)
        return

    def gainQuest(self, cards):
        self.quests.extend(cards)
        return

    def completeQuest(self, index):
        if self.resources < self.quests[index].cost:
            print('ERROR quest cost too high')
            return
        quest = self.quests.pop(index)
        self.resources = self.resources - quest.cost
        self.resources = self.resources + quest.reward
        #do callbacks?
        # if has one of 5 plot quests completed and quest.questtype == plotquest.questtype
        # then score 2 VP
        # if have one of 5 if action plot quest completed
        # then check if action matches trigger reward bonus
        self.completed.append(quest)
        return

    def buyBuilding(self, building):
        building.buy(self)
        self.buildings.append(building)
    
    def receiveResources(self, effects):
        increment = RVector(0,0,0,0,0,0,0,0,0)
        for e in effects:
            if e.choice == 0:
                increment = increment + RVector(e.coin,e.white,e.black,e.orange,e.purple,0,0,0,0)
            else:
                for i in range(e.choice):
                    increment = self.chooseToken(increment,e.coin, e.white, e.black, e.orange, e.purple)
            increment = increment + RVector(0,0,0,0,0,e.vp,e.intrigue,e.quest,0)
        self.resources = self.resources + increment

    def chooseToken(self, pool, c, w, b, o, p):
        #make choice
        choice = random.randint(0,4)
        while (choice == 0 and c == 0) or (choice == 1 and w == 0) or (choice == 2 and b == 0) or (choice == 3 and o == 0) or (choice == 4 and p == 0):
            choice = random.randint(0,4)
        c=c if choice == 0 else 0
        w=w if choice == 1 else 0
        b=b if choice == 2 else 0
        o=o if choice == 3 else 0
        p=p if choice == 4 else 0
        pool = pool + RVector(c,w,b,o,p,0,0,0,0)
        return pool
    
    def chooseFromPile(self, quests):
        #pick a quest
        #add quest to open quests
        #return remaining
        self.gainQuest([quests.pop()])
        return quests

    def chooseQuestType(self):
        #have current player choose a quest type
        return 'Arcana'

    def chooseQuest(self):
        return 0

    def playAgent(self):
        # check if they have either plot quests RECOVER THE MAGISTER"S ORB
        return
    
    def playAmbassador(self, buildings):
        return buildings[random.randint(0,len(buildings)-1)]
    
    def chooseIntrigue(self):
        # choose and return an intrigue card
        return

class Group():
    #AI models will be tied to a player color,
    # order will be randomized?
    #first is a color
    def __init__(self, numplayers, numai, lords, colors = ['yellow','grey','blue','green','red'], pcs = []):
        if numplayers != numai + len(pcs):
            print('ERROR player.py line 73 Group __init__ group size mismatch')
        
        self.numplayers = numplayers
        for pc in pcs:
            if pc.color not in colors:
                print('ERROR')
                return
            colors.remove(pc.color)
        random.shuffle(colors)
        while len(colors) != numai:
            colors.pop()
        self.colors = colors
        self.players = [Player(color, numagents[numplayers]) for color in self.colors]
        self.players.extend(pcs)
        for p in self.players:
            p.assignLord(lords.draw())
        self.first = 0
        self.current = self.first
    
    def __repr__(self):
        return '\n'.join(str(p) for p in self.players)
    
    def __str__(self):
        return '\n'.join(str(p) for p in self.players)
    
    def getSpecific(self, color):
        return self.players[self.colors.index(color)]

    def getCurrent(self):
        return self.players[self.current]

    def goTo(self, color):
        self.current = self.colors.index(color)

    def goToFirst(self):
        self.current = self.first

    def goToLast(self):
        self.current = self.numplayers - 1
    
    def nextPlayer(self):
        self.current = self.current + 1 
        if self.current >= self.numplayers:
            self.current = 0

    def resetAgents(self):
        for p in self.players:
            p.numagents = p.totalagents

    def roundFive(self):
        for p in self.players:
            p.totalagents += 1