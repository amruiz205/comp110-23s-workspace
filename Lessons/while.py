

cards: str = "5235"

card_indx: int = 0

low_card: int = int(cards[0])


while card_indx < 4:
    current_card: int = int(cards[card_indx])
    if (current_card < low_card):
        low_card = current_card
    card_indx = card_indx + 1
print(low_card)





