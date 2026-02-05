import random

hands = ["hearts", "diamonds", "spades", "clubs"]
cards = []
values = []
TotalValues = [i for i in range(1, 14)]
FaceValue = []
heartSuit = 0
diamondSuit = 0
spadeSuit = 0
clubSuit = 0

def pickHands():
    global cards
    for i in range(5):
        hand = random.choice(hands)
        number = random.randint(1, 13)
        cards.append(hand)
        values.append(number)

def displayHand():
    global cards, values
    for i in range(0, 5):
        print(str(cards[i]) + " of " + str(values[i]))

def addCardCount():
    global FaceValue, count
    TotalCardValue = values[0] + values[1] + values[2] + values[3] + values[4]
    print("the total value of all the cards is " + str(TotalCardValue))
    for i in TotalValues:
        NumValues = 0
        if i in values:
            NumValues += values.count(i)
        FaceValue.append(NumValues)
    print("Face value count: " + str(FaceValue))

def countSuits():
    global heartSuit, diamondSuit, spadeSuit, clubSuit
    for i in range(len(cards)):
        if "hearts" in cards:
            heartSuit += 1
            cards.remove("hearts")
        if "diamonds" in cards:
            diamondSuit += 1
            cards.remove("diamonds")
        if "spades" in cards:
            spadeSuit += 1
            cards.remove("spades")
        if "clubs" in cards:
            clubSuit += 1
            cards.remove("clubs")
    print("hearts: " + str(heartSuit), "diamonds: " + str(diamondSuit), "spades: " + str(spadeSuit), "clubs: " + str(clubSuit))

pickHands()

print(cards)
print(values)

print("----- Current Hand -----")

displayHand()

addCardCount()
countSuits()

print("goodbye")