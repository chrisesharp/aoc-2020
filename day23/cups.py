class Cups:
    def __init__(self, cups):
        self.cups = [int(n) for n in cups]
    
    def play(self, pt2=False):
        cups = self.cups
        labels = {}
        num_cups = 1000000 if pt2 else len(self.cups)
        turns = 10000000 if pt2 else 100

        for i in range(len(self.cups)):
            labels[cups[i]] = cups[i + 1] if i != len(self.cups) - 1  else max(cups) + 1
        
        if pt2:
            for i in range(len(cups) + 1, num_cups):
                labels[i] = (i + 1)
            labels[num_cups] = cups[0]
        else:
            labels[cups[num_cups - 1]] = cups[0]

        cur = cups[0]

        for i in range(turns):
            cup1 = labels[cur]
            cup2 = labels[cup1]
            cup3 = labels[cup2]

            labels[cur] = labels[cup3]
            dest = cur - 1 if cur > 1 else num_cups

            while dest in [cup1, cup2, cup3]:
                dest = dest - 1 if dest > 1 else num_cups

            labels[cup3] = labels[dest]
            labels[dest] = cup1
            cur = labels[cur]

        if pt2:
            return (labels[1] * labels[labels[1]] )
        else:
            result = ""
            curr = labels[1]
            while curr != 1:
                result += str(curr)
                curr = labels[curr]
            return result
    
if __name__ == '__main__':
    data = "362981754"
    game = Cups(data)
    print("Part 1:",game.play())
    print("Part 2:", game.play(True))