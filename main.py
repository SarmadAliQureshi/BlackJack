import random
class Main_Class():
    suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
    ranks = ['Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace']
    def deck_creator(self):
        self.suits=Main_Class.suits
        self.ranks=Main_Class.ranks
        self.deck = {}
        ranks_dictionary={}
        # dict(ranks_dictionary)
        count=2
        for r in self.ranks:
            if count<=10:
                ranks_dictionary[r]=count
                count=count+1
            elif count>10 and count<14:
                ranks_dictionary[r]=10
                count=count+1
            elif count==14:
                ranks_dictionary[r]=11

        for i in self.suits:
            self.deck[i]=ranks_dictionary
        return self.deck

# mc=Main_Class()
# print(mc.ranks)
# a = (mc.deck_creator())
# print()
    # def random_card_picker(self):
    #
    #     a = (deck['Hearts'])
    #     # print(a)
    #
    #     # d=deck.fromkeys(range(10))
    #     suit_computer = random.sample(list(deck),1)
    #     # print(suit_computer[0])
    #     card_number = ((random.sample(list(a),1)))
    #     # print(card_number[0])
    #     # print(deck[str(suit_computer[0])][card_number[0]])
    #     card_in_hand = deck[str(suit_computer[0])][str(card_number[0])]
    #     del deck[str(suit_computer[0])][str(card_number[0])]
    #     print(deck)

class Players(Main_Class):
    def __init__(self):
        # creating the object of main class
        self.mc= Main_Class()
        # calling that object of main class which was created above and accessing function of that class
        self.main_deck=self.mc.deck_creator()
        print(self.main_deck)
        self.computer()
        self.human()
        # self.Main_Class.deck_creator()

    def computer(self):
        self.random_card_picker(self.main_deck)

    def human(self):
        i = 0
        for i in range(0, 2):
            self.random_card_picker(self.main_deck)

    def random_card_picker(self, main_deck):
        self.deck=main_deck
        a = (self.deck['Hearts'])
        # print(a)
        results=[]
        # d=deck.fromkeys(range(10))
        suit_computer = random.sample(list(self.deck),1)
        results.append(suit_computer)
        # print(suit_computer[0])
        card_number = ((random.sample(list(a),1)))
        results.append(card_number)
        # print(card_number[0])
        # print(deck[str(suit_computer[0])][card_number[0]])
        card_in_hand = self.deck[str(suit_computer[0])][str(card_number[0])]
        results.append(card_in_hand)
        del self.deck[str(suit_computer[0])][str(card_number[0])]
        print(results)
        print(self.deck)


p=Players()
