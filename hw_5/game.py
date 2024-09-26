import logic_game
from decouple import config

money = int(config('MY_MONEY'))
while True:
    print(f"Ваш текущий капитал: {money}")
    slot_number = int(input("Введите номер слота от 1 до 10: "))
    bet_amount = int(input("Введите сумму ставки: "))
    money += logic_game.play_game(slot_number, bet_amount)
    print(f"Ваш текущий капитал: {money}")
    play_again = input("Хотите ли вы сыграть еще? (да/нет): ")
    if play_again.lower() != "да":
        break
print(f"Игра окончена. Ваш конечный капитал: {money}")
if money > 1000:
    print('Вы в выигрыше!')
else:
    print('Вы в проигрыше!')
