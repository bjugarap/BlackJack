import random, sys, os 

class Player:
    def __init__(self, name: str, is_dealer: bool = False) -> None:
         self.name = name
         self.cards = {}
         self.is_bust = False
         self.is_dealer = is_dealer

    def sum_of_cards(self) -> int:
        self.cards_sum = 0
        ace_exist = False
        for card, value in self.cards.items():
            if ace_exist == False and value == 11 and self.cards_sum <= 10:
                self.cards_sum += value
                ace_exist = True
            elif ace_exist == False and value == 11 and self.cards_sum > 10:
                value = 1
                self.cards_sum += value
                ace_exist = True
            elif ace_exist == True and value == 11:
                value = 1
                self.cards_sum += value
            elif ace_exist == True:
                self.cards_sum += value
                if self.cards_sum > 21:
                    self.cards_sum = sum(self.cards.values()) -10
            else:
                self.cards_sum += value
            
        return self.cards_sum

card_deck = {"A of hearts" : 11,
             "K of hearts" : 10,
             "Q of hearts" : 10,
             "J of hearts" : 10,
             "10 of hearts" : 10,
             "9 of hearts" : 9,
             "8 of hearts" : 8,
             "7 of hearts" : 7,
             "6 of hearts" : 6,
             "5 of hearts" : 5,
             "4 of hearts" : 4,
             "3 of hearts" : 3,
             "2 of hearts" : 2,
             "A of diamonds" : 11,
             "K of diamonds" : 10,
             "Q of diamonds" : 10,
             "J of diamonds" : 10,
             "10 of diamonds" : 10,
             "9 of diamonds" : 9,
             "8 of diamonds" : 8,
             "7 of diamonds" : 7,
             "6 of diamonds" : 6,
             "5 of diamonds" : 5,
             "4 of diamonds" : 4,
             "3 of diamonds" : 3,
             "2 of diamonds" : 2,
             "A of clubs" : 11,
             "K of clubs" : 10,
             "Q of clubs" : 10,
             "J of clubs" : 10,
             "10 of clubs" : 10,
             "9 of clubs" : 9,
             "8 of clubs" : 8,
             "7 of clubs" : 7,
             "6 of clubs" : 6,
             "5 of clubs" : 5,
             "4 of clubs" : 4,
             "3 of clubs" : 3,
             "2 of clubs" : 2,
             "A of spades" : 11,
             "K of spades" : 10,
             "Q of spades" : 10,
             "J of spades" : 10,
             "10 of spades" : 10,
             "9 of spades" : 9,
             "8 of spades" : 8,
             "7 of spades" : 7,
             "6 of spades" : 6,
             "5 of spades" : 5,
             "4 of spades" : 4,
             "3 of spades" : 3,
             "2 of spades" : 2
             }

def clear_terminal() -> None:
    if os.name == 'nt': #Windows
        _ = os.system("cls")
    else:
        _ = os.system("clear") #macOS and Linux

def get_card() -> dict:
        card = {}
        random_key = random.choice(list(card_deck.keys()))
        random_value = card_deck[random_key]

        card[random_key] = random_value

        card_deck.pop(random_key)

        return card


def deal_cards(Player: Player) -> None:
        player.cards.update(get_card())


def show_cards() -> None:
    # os.system("cls")
    clear_terminal()

    for player in players:
        if player.is_dealer == True:
            print(f"Dealer has: {list(player.cards.keys())}")
            print(f"Total: {player.sum_of_cards()} \n")

    for player in players:
        if player.is_dealer == False:
            print(f"{player.name} has: {list(player.cards.keys())}")  
            print(f"Total: {player.sum_of_cards()} \n")
         

def show_winner(players: list[Player]) -> None:
    print("------------------------")
    print("      Game Results      ")
    print("------------------------")

    dealer_bust = False
    dealer_total = sum([player.sum_of_cards() for player in players if player.is_dealer == True])


    if dealer_total > 21:
        dealer_bust = True

    for player in players:
      
        if dealer_total > player.sum_of_cards() and dealer_bust != True:
            print(f"{player.name} lost. Dealer wins!")
        elif dealer_bust == False and player.is_bust == True and player.is_dealer == False:
            print(f"{player.name} busted. Dealer wins!")
        elif dealer_total == player.sum_of_cards() and player.is_dealer == False:
            print(f"{player.name} PUSH with Dealer!")
        elif dealer_total < player.sum_of_cards() and player.is_dealer == False and player.is_bust == False:
            print(f"{player.name} wins!")
        elif dealer_bust == True and player.is_dealer == False and player.is_bust == False:
            print(f"{player.name} wins!")
        elif player.is_bust == True and player.is_dealer == False:
            print(f"{player.name} busted. Dealer wins") 



if __name__ == "__main__":

    # Get number of players
    num_players = int(input("How many players? "))

    # Create instances of players
    players = [Player(f"Player {i + 1}", is_dealer=False) for i in range(num_players)]
    players.append(Player("Dealer", is_dealer=True))

    # Deal first pair of cards. 
    for player in players * 2:
        deal_cards(player)
 
    show_cards()

    for player in players:
        if player.is_dealer == False:
            while player.is_bust == False:

                if player.sum_of_cards() == 21:
                    break

                hit_or_stay = input(f"{player.name} hit or stay? : ")
 
                if hit_or_stay.lower() == "hit":
                    deal_cards(player)
                    show_cards()

                elif hit_or_stay.lower() == 'stay' :
                    break
                
                if player.sum_of_cards() > 21:
                    player.is_bust = True
                    print(f"{player.name} has more than 21. {player.name} Bust!!!")
                    break
        
        if player.is_dealer == True:
            while player.is_bust == False:
                if player.sum_of_cards() >= 17 and player.sum_of_cards() <= 21:
                    break
                while player.sum_of_cards() < 17:
                    deal_cards(player)
                    if player.sum_of_cards() > 21:
                        player.is_bust = True
                        break
                    elif player.sum_of_cards() == 21:
                        break
            
    show_cards()
    show_winner(players)


