import unittest
from card_and_deck import Card, Deck


class CardTest(unittest.TestCase):
    def setUp(self):
        self.card = Card("10", "Diamonds")

    def test_init(self):
        """card should have a value and a suit"""
        self.assertEqual(self.card.value, "10")
        self.assertEqual(self.card.suit, "Diamonds")

    def test_repr(self):
        """representation of card should equal 'VALUE of SUIT'"""
        self.assertEqual(repr(
            self.card), "10 of Diamonds")     # also possible to do: self.card.__repr__()


class DeckTest(unittest.TestCase):
    def setUp(self):
        self.deck = Deck()

    def test_init(self):
        """deck should have a cards attribute, which is a list of 52 cards"""
        self.assertTrue(isinstance(self.deck.cards, list))
        self.assertEqual(len(self.deck.cards), 52)

    def test_init2(self):
        """a chosen card should be in a deck"""
        self.assertIn("2 of Diamonds", (repr(x) for x in self.deck.cards))

    def test_repr(self):
        """representation of deck should equal 'Deck of COUNT cards'"""
        self.assertEqual(repr(self.deck), "Deck of 52 cards")

    def test_count(self):
        """count should return a number of cards left in the deck"""
        self.assertEqual(self.deck.count(), 52)
        self.deck.cards.pop()
        self.assertEqual(self.deck.count(), 51)

    def test_raise_error(self):
        """testing the raise of a ValueError"""
        self.deck.deal_hand(52)
        with self.assertRaises(ValueError):
            self.deck._deal(1)


if __name__ == "__main__":
    unittest.main()
