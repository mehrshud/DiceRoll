
import random

class Player:
    def __init__(self, name):
        self.name = name
        self.score = 0

class DiceRoll:
    def __init__(self):
        self.players = []

    def add_player(self, player):
        self.players.append(player)

    def roll_dice(self):
        return random.randint(1, 6)

    def play_game(self):
        for player in self.players:
            input(f'{player.name}, press Enter to roll the dice...')
            roll = self.roll_dice()
            print(f'{player.name} rolled a {roll}')
            player.score += roll
        self宣告_winner()

    def 宣告_winner(self):
        max_score = max(player.score for player in self.players)
        winners = [player.name for player in self.players if player.score == max_score]
        if len(winners) == 1:
            print(f'The winner is {winners[0]} with a score of {max_score}')
        else:
            print(f'The winners are {", ".join(winners)} with a score of {max_score}')

def main():
    game = DiceRoll()
    num_players = int(input('Enter the number of players: '))
    for i in range(num_players):
        name = input(f'Enter player {i+1} name: ')
        game.add_player(Player(name))
    game.play_game()

if __name__ == '__main__':
    main()
