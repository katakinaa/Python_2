from random import randint


def play_game(slot_number, bet_amount):
    winning_slot = randint(1, 10)
    if slot_number == winning_slot:
        return 2 * bet_amount
    else:
        return -bet_amount
