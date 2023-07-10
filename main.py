import random

SUITS = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
RANKS = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King', 'Ace']


def distribute_cards_x(x):
  deck = [(rank, suit) for suit in SUITS for rank in RANKS]

  # Shuffle the deck
  random.shuffle(deck)

  # Distribute 5 random cards to 4 people
  people = ['Person 1', 'Person 2', 'Person 3', 'Person 4']
  hands = {person: [] for person in people}

  for _ in range(x):
      for person in people:
          card = deck.pop()
          hands[person].append(card)
  return hands


def compare_cards(card1, card2, card3, card4):
    ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King', 'Ace']
    values = {rank: i+1 for i, rank in enumerate(ranks)}

    cards = [card1, card2, card3, card4]

    max_card = cards[0]
    for card in cards[1:]:
        if values[card[0]] > values[max_card[0]]:
            max_card = card

    return max_card



hands = distribute_cards_x(5)

for person, cards in hands.items():
    print(person + ":")
    for card in cards:
        print(card)
print("---------------------------")

decided_color = random.choice(SUITS)
print('decided_color', decided_color)




max_card = compare_cards(hands['Person 1'][0], hands['Person 2'][0], hands['Person 3'][0], hands['Person 4'][0])
print('max_card---->', max_card)

# hands = distribute_cards_x(4)

# for person, cards in hands.items():
#     print(person + ":")
#     for card in cards:
#         print(card)

# print("---------------------------")

# hands = distribute_cards_x(4)

# for person, cards in hands.items():
#     print(person + ":")
#     for card in cards:
#         print(card)