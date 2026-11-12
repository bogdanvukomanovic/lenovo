from collections import Counter

class Hand():

    joker_rule = False

    def __init__(self, hand, bid):
        self.hand = hand
        self.type = self.deduce_type(list(Counter(self.hand).values()))
        self.bid = bid

    def deduce_type(self, count: list[int]) -> str:

        if self.five(count):
            return "5OAK"

        if self.four(count):
            return "4OAK"

        if self.full_house(count):
            return "FH"

        if self.three(count):
            return "3OAK"

        if self.two_pair(count):
            return "2P"

        if self.one_pair(count):
            return "1P"

        return "HC"

    def five(self, count: {str, int}) -> bool:
        return True if len(count) == 1 else False

    def four(self, count: {str, int}) -> bool:
        return any(x == 4 for x in count)

    def full_house(self, count: {str, int}) -> bool:

        if len(count) != 2:
            return False

        return (count[0] == 3 and count[1] == 2) or (count[0] == 2 and count[1] == 3)

    def three(self, count: {str, int}) -> bool:
        return any(x == 3 for x in count)

    def two_pair(self, count: {str, int}) -> bool:

        if len(count) != 3:
            return False

        return (count[0] == 2 and count[1] == 2) or (count[0] == 2 and count[2] == 2) or (count[1] == 2 and count[2] == 2)

    def one_pair(self, count: {str, int}) -> bool:
        return any(x == 2 for x in count)

    def joker(self):

        if 'J' in self.hand:
            count = Counter(self.hand)
            jokers = count.pop('J')
            if jokers != 5:
                count[count.most_common()[0][0]] += jokers
                self.type = self.deduce_type(list(count.values()))


    def __str__(self) -> str:
        return self.hand + " : " + str(self.bid) + " > " + self.type

    def __eq__(self, other: object) -> bool:

        if not isinstance(other, Hand):
            return NotImplemented

        return self.hand == other.hand

    def __lt__(self, other: object) -> bool:

        if not isinstance(other, Hand):
            return NotImplemented

        i, n = 0, len(self.hand)
        if not Hand.joker_rule:
            strength = { 'A': 13, 'K': 12, 'Q': 11, 'J': 10, 'T': 9, '9': 8, '8': 7, '7': 6, '6': 5, '5': 4, '4': 3, '3': 2, '2': 1 }
        else:
            strength = { 'A': 13, 'K': 12, 'Q': 11, 'J': 0, 'T': 9, '9': 8, '8': 7, '7': 6, '6': 5, '5': 4, '4': 3, '3': 2, '2': 1 }

        while i < n:

            if strength[self.hand[i]] < strength[other.hand[i]]:
                return True
            elif strength[self.hand[i]] > strength[other.hand[i]]:
                return False

            i += 1

        return True

def part_one(hands: list[Hand]) -> int:

    gruop = {
        "5OAK"  : [],
        "4OAK"  : [],
        "FH"    : [],
        "3OAK"  : [],
        "2P"    : [],
        "1P"    : [],
        "HC"    : []
    }

    for hand in hands:
        gruop[hand.type].append(hand)

    ranking = []
    ranking += sorted(gruop["HC"])
    ranking += sorted(gruop["1P"])
    ranking += sorted(gruop["2P"])
    ranking += sorted(gruop["3OAK"])
    ranking += sorted(gruop["FH"])
    ranking += sorted(gruop["4OAK"])
    ranking += sorted(gruop["5OAK"])

    winnings = 0
    for i, rank in enumerate(ranking):
        winnings += (i + 1) * rank.bid

    return winnings

def part_two(hands: list[Hand]) -> int:

    gruop = {
        "5OAK"  : [],
        "4OAK"  : [],
        "FH"    : [],
        "3OAK"  : [],
        "2P"    : [],
        "1P"    : [],
        "HC"    : []
    }

    for hand in hands:
        hand.joker()
        gruop[hand.type].append(hand)

    ranking = []
    ranking += sorted(gruop["HC"])
    ranking += sorted(gruop["1P"])
    ranking += sorted(gruop["2P"])
    ranking += sorted(gruop["3OAK"])
    ranking += sorted(gruop["FH"])
    ranking += sorted(gruop["4OAK"])
    ranking += sorted(gruop["5OAK"])

    winnings = 0
    for i, rank in enumerate(ranking):
        winnings += (i + 1) * rank.bid

    return winnings

with open("in.txt") as f:
    content = f.read().split('\n')

hands = []
for line in content:
    line = line.split()
    hands.append(Hand(line[0], int(line[1])))

Hand.joker_rule = False
print(part_one(hands))
Hand.joker_rule = True
print(part_two(hands))