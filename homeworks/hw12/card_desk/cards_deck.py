import random


class Card:
    number_list = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
    mast_list = ['Hearts', 'Diamonds', 'Clubs', 'Spades']

    def __init__(self, number, mast):
        self.number = number
        self.mast = mast


class CardsDeck:
    def __init__(self):
        self.cards = []
        self._initialize_deck()

    def _initialize_deck(self):
        self.cards = []
        for mast in Card.mast_list:
            for number in Card.number_list:
                self.cards.append(Card(number, mast))
        self.cards.append(Card('Joker', 'Red'))
        self.cards.append(Card('Joker', 'Black'))

    def shuffle(self):
        random.shuffle(self.cards)

    def get_card(self, card_number):
        validated_num = self._card_validator(card_number)
        card_index = validated_num - 1
        card = self.cards[card_index]
        del self.cards[card_index]
        return card

    def get_remaining_cards(self):
        return self.cards

    def _card_validator(self, card_number):
        if not isinstance(card_number, int):
            raise ValueError("Error: enter a card number from 1 to 54")
        if card_number < 1 or card_number > 54:
            raise ValueError("Error: enter a card number from 1 to 54")
        return card_number
