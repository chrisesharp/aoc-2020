class Cards:
    def __init__(self, hand_one=[], hand_two=[]):
        self.player_1 = hand_one
        self.player_2 = hand_two
    
    def deal(self, data):
        player_1 = data[0].split('\n')[1:]
        player_2 = data[1].split('\n')[1:]
        self.player_1 = list(map(int, player_1))
        self.player_2 = list(map(int, player_2))

    def play(self):
        deck = len(self.player_1) + len(self.player_2)
        game_over = False
        while not game_over:
            p1 = self.player_1.pop(0)
            p2 = self.player_2.pop(0)
            if p1 > p2:
                self.player_1.append(p1)
                self.player_1.append(p2)
            else:
                self.player_2.append(p2)
                self.player_2.append(p1)
            game_over = (len(self.player_1) == deck or len(self.player_2) == deck)
        self.winner = self.player_1 if len(self.player_1) else self.player_2
    
    def score(self):
        total = 0
        top = len(self.winner)
        for i, val in enumerate(self.winner):
            total += (top - i) * val
        return total

def to_key(hand):
    return ":".join(map(str,hand))

class RecursiveCombat(Cards):
    def __init__(self, hand_one=[], hand_two=[]):
        super().__init__(hand_one, hand_two)
        self.hands_one = set()
        self.hands_two = set()
    
    def play(self):
        deck = len(self.player_1) + len(self.player_2)
        game_over = False
        while not game_over:
            h1 = to_key(self.player_1)
            h2 = to_key(self.player_2)
            if h1 in self.hands_one or h2 in self.hands_two:
                self.winner = self.player_1
                return True
            self.hands_one.add(h1)
            self.hands_two.add(h2)

            p1 = self.player_1.pop(0)
            p2 = self.player_2.pop(0)
            p1_win = p1 > p2 if len(self.player_1) < p1 or len(self.player_2) < p2 else RecursiveCombat(self.player_1[:p1],self.player_2[:p2]).play()
            if p1_win:
                self.player_1.extend([p1,p2])
            else:
                self.player_2.extend([p2,p1])
            game_over = (len(self.player_1) == deck or len(self.player_2) == deck)
        
        if len(self.player_1) == deck:
            self.winner = self.player_1
            return True
        else:
            self.winner = self.player_2
            return False

if __name__ == '__main__':
    data = open("input.txt","r").read().split("\n\n")
    game = Cards()
    game.deal(data)
    game.play()
    print("Part 1:",game.score())
    game = RecursiveCombat()
    game.deal(data)
    game.play()
    print("Part 2:", game.score())