import random


class Card:
    def __init__(self, dignities, kind):
        self.dignities = dignities
        self.kind = kind


class Deck:
    def __init__(self):
        dignities = ['Туз', 2, 3, 4, 5, 6, 7, 8, 9, 10, 'Валет', 'Дама', 'Король']
        kind = ['пики', 'крести', 'черви', 'буби']
        self.deck_list = [Card(dig, k) for dig in dignities for k in kind]

    def dispensing(self):
        card = random.choice(self.deck_list)
        self.deck_list.remove(card)
        return card


class Player:
    def __init__(self, name):
        self.name = name
        self.cards = []

    def append_card(self, card):
        if card.dignities == 'Туз':
            self.cards.insert(0, card)
        else:
            self.cards.append(card)


    def calculation_card(self):
        total = 0
        for card in self.cards[::-1]:
            if isinstance(card.dignities, int):
                total += int(card.dignities)
            elif card.dignities in ['Валет', 'Дама', 'Король']:
                total += 10
            else:
                if total <= 10:
                    total += 11
                elif total > 10:
                    total += 1
        return total


    def print_card(self):
        print(f'\nУ {self.name} следующие карты:')
        for card in self.cards:
            print(card.dignities, card.kind, end='\n')


deck = Deck()
player1 = Player('Василий(я)')
player2 = Player('Компьютер(а)')

for _ in range(2):
    player1.append_card(deck.dispensing())
    player2.append_card(deck.dispensing())

try:
    while True:
        player1.print_card()
        print(f'У {player1.name} {player1.calculation_card()}')
        accord = input('Хотите взять ещё карту? да/нет: ')
        if accord == 'да':
            player1.append_card(deck.dispensing())
        else:
            break
        if player1.calculation_card() > 21:
            raise Exception
    while True:
        if player2.calculation_card() <= 16:
            player2.append_card(deck.dispensing())
        else:
            break
except Exception:
    print(f'\nУ {player1.name} {player1.calculation_card()} - перебор. {player2.name} победил.')
else:
    if (player1.calculation_card() == 21 and player2.calculation_card() != 21) or player2.calculation_card() > 21 or (player1.calculation_card() > player2.calculation_card()):
        print(f'\n{player1.name} победил. У {player2.name} {player2.calculation_card()}')
    elif (player2.calculation_card() == 21 and player1.calculation_card() != 21) or (player1.calculation_card() < player2.calculation_card()):
        print(f'\n{player2.name} победил. У {player1.name} {player1.calculation_card()}')
    elif player2.calculation_card() == player1.calculation_card():
        print('Ничья!')
