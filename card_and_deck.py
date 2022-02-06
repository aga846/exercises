from random import shuffle


class Card:
    def __init__(self, value, suit):
        self.value = value
        self.suit = suit

    def __repr__(self):
        return f"{self.value} of {self.suit}"


class Deck:
    def __init__(self):
        suits = ["Hearts", "Diamonds", "Clubs", "Spades"]
        values = ["A", "2", "3", "4", "5", "6", "7", "8",
                  "9", "10", "J", "Q", "K"]
        self.cards = [Card(value, suit) for suit in suits for value in values]
        self.out_of_deck = []

    def __repr__(self):
        return f"Deck of {self.count()} cards"

    def count(self):
        return len(self.cards)

    def _deal(self, num):
        count = self.count()
        actual = min([count, num])
        if count == 0:
            raise ValueError("All cards have been dealt")
        cards = self.cards[-actual:]
        self.cards = self.cards[:-actual]
        self.out_of_deck.extend(cards)
        return cards

    def deal_card(self):
        return self._deal(1)[0]

    def deal_hand(self, hand_size):
        return self._deal(hand_size)

    def out_print(self):
        return f"Cards out of deck: {self.out_of_deck}"

    def shuffle(self):
        if self.count() < 52:
            raise ValueError("Only full decks can be shuffled")
        shuffle(self.cards)
        return self

    def reset(self):
        self.cards.extend(self.out_of_deck)
        self.out_of_deck = []


deck1 = Deck()
print(type(deck1.cards[0]))
print(type(Card("2", "Diamonds")))
if Card("2", "Diamonds") in deck1.cards:
    print("True")

'''deck1.shuffle()
card = deck1.deal_card()
print(card)
hand = deck1.deal_hand(5)
print(hand)
print(deck1.out_print())
'''
