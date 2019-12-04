# choice and any are represented bythe tokens and the choice params, 
# where the tokens shoe the options and the choice is the number of times the choice and be made
# any is a choice between all 4 types of adeventurers

class RVector():
    coin = 0
    white = 0
    black = 0
    orange = 0
    purple = 0
    vp = 0
    intrigue = 0
    quest = 0
    choice = 0

    def __init__(self, c, w, b, o, p, v, i, q, n):
        self.coin = c
        self.white = w
        self.black = b
        self.orange = o
        self.purple = p
        self.vp = v
        self.intrigue = i
        self.quest = q
        self.choice = n
    
    def __repr__(self):
        pieces = []
        if self.coin != 0:
            pieces.append(('gives' if self.coin > 0 else 'costs') +
                          (' {0!s} coin').format(abs(self.coin)) + 's' if abs(self.coin) > 1 else '')
        if self.white != 0:
            pieces.append(('gives' if self.white > 0 else 'costs') +
                          (' {0!s} white').format(abs(self.white)) + 's' if abs(self.white) > 1 else '')
        if self.black != 0:
            pieces.append(('gives' if self.black > 0 else 'costs') +
                          (' {0!s} black').format(abs(self.black)) + 's' if abs(self.black) > 1 else '')
        if self.orange != 0:
            pieces.append(('gives' if self.orange > 0 else 'costs') +
                          (' {0!s} orange').format(abs(self.orange)) + 's' if abs(self.orange) > 1 else '')
        if self.purple != 0:
            pieces.append(('gives' if self.purple > 0 else 'costs') +
                          (' {0!s} purple').format(abs(self.purple)) + 's' if abs(self.purple) > 1 else '')
        if self.vp != 0:
            pieces.append(('gives' if self.vp > 0 else 'costs') +
                          (' {0!s} vp').format(abs(self.vp)) + 's' if abs(self.vp) > 1 else '')
        if self.intrigue != 0:
            pieces.append(('gives' if self.intrigue > 0 else 'costs') +
                          (' {0!s} intrigue').format(abs(self.intrigue)) + 's' if abs(self.intrigue) > 1 else '')
        if self.quest != 0:
            pieces.append(('gives' if self.quest > 0 else 'costs') +
                          (' {0!s} quest').format(abs(self.quest)) + 's' if abs(self.quest) > 1 else '')
        if self.choice != 0:
            pieces.append(('gives' if self.choice > 0 else 'costs') +
                          (' {0!s} choice').format(abs(self.choice)) + 's' if abs(self.choice) > 1 else '')
        return ', '.join(pieces)

    def __add__(self, other):
        self.coin += other.coin
        self.white += other.white
        self.black += other.black
        self.orange += other.orange
        self.purple += other.purple
        self.vp += other.vp
        self.intrigue += other.intrigue
        self.quest += other.quest
        self.choice += other.choice
