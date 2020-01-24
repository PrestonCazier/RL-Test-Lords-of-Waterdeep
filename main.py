import random
import sys

import pandas as pd
from itertools import cycle

import building
import player
import quest
import lord
import intrigue
from resourcevector import RVector

#Builder's hall is a list of length 4 containing tuples
#ele0: building; ele1: cost; ele2:vp; ele3; buy effects

typeslist = ['Building', 'Commerce',
             'Skullduggery', 'Warfare', 'Piety', 'Arcana', 'Mandatory']
startingbuildings = ['Cliffwatch Inn1', 'Cliffwatch Inn2', 'Cliffwatch Inn3', 'Waterdeep Harber1',
                    'Waterdeep Harber2', 'Waterdeep Harber3', 'Field of Triumph', 'Blackstaff Tower',
                    'Castle Waterdeep', 'Builder\'s Hall', 'Aurora\'s Realms Shop',
                    'The Plinth', 'The Grinning Lion Tavern']
startingQuests = 2
startingIntrigue = 2
innSize = 4
hallSize = 4
lords = None
quests = None
intrigues = None
buildings = None
board = None
inn = []
hall = []
players = None

def roll():
    return random.randint(0,5)

def checkArgs():
    #whether tokens and resources should be limited or unlimited
    return

def palaceOfWaterDeep(players, player):
    for p in players:
        p.setAmbassador(p == player)

def buildersHall():
    
    return
            
def initializeGame(numplayers, numai):
    lords = lord.Deck()
    quests = quest.Deck()
    intrigues = intrigue.Deck()
    buildings = building.Deck()
    board = buildings.grabInitialBuildings(startingbuildings)
    #shuffle decks
    lords.shuffle()
    quests.shuffle()
    intrigues.shuffle()
    buildings.shuffle()
    #make players
    players = player.Group(numplayers, numai, lords)
    #determine first player
        #pick someone
        #cycle list to that person
        #has to come before money handout
    #deal quests
    for player in players:
        player.gainQuest([quests.pop() for i in range(startingQuests)])
    #deal intrigue
    for player in players:
        player.gainQuest([quests.pop() for i in range(startingIntrigue)])
    #hand out initial currency
    startingGold = RVector(4,0,0,0,0,0,0,0,0)
    players.goToFirst()
    for i in range(numplayers):
        players.getCurrent().recieveResources(startingGold)
        startingGold.coin += 1
        players.nextPlayer()
    #add quests to the inn
    inn = [quests.draw() for i in range(innSize)]
    #builders hall
    hall = [buildings.draw() for i in range(hallSize)]
    #finally add callbacks
    deck.buildings['The Stone House'].extraeffects[lambda board, player: len(board) - 13] = [board]
    deck.buildings['The Zoarstar'].extraeffects[lambda board, player:player.chooseBuilding(
        [b for b in board if b.occupant != player])] = [board]
    deck.buildings['The Palace of Waterdeep'].extraeffects[palaceOfWaterDeep] = [players]
    return

def main(numplayers, numai):
    #shuffle decks using shuffle(deckobj, times) {for times random.shuffle(deck)}
    initializeGame()
    for round in range(8):
        #update phase
        print('')
        #reset phase
        print('')
        #ambassador phase
        print('')
        #play phase
        print('')
        while agentsLeft():
            print('')
        #reassign phase
        print('')
    return

initializeGame()

if '__name__' == '__main__':
    checkArgs()

    print('Welcome to Lords of Waterdeep RL Experiment')
    print('Let\'s start by selecting the total number of players that are going to play')
    numplayers = input('Please enter your selection(2-5):')
    print('Great, it seems you selected {numplayers} total players')
    numai = input('Now how many of these will be AIs?')

    main(numplayers, numai)
