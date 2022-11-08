import random
from datetime import datetime

from game import game
from player import Player
from property import Property

properties = 20  # Quantity of properties that should be on the table

rounds_finished = []
winners = []
if __name__ == '__main__':
    for _ in range(300):
        random.seed(datetime.now())
        personas = ['impulsivo', 'exigente', 'cauteloso', 'aleatorio']
        random.shuffle(personas)  # shuffling the personas before each game
        r, w = game(table=[Property() for _ in range(properties)],
                    properties_qnt=properties,
                    players=[Player(p) for p in personas],
                    original_order=personas)
        rounds_finished.append(r)
        winners.append(w)


winner_count = {p: winners.count(p) for p in personas}
all_time_winner = sorted(winner_count, key=winner_count.get)
print(f'timeout rounds quantity: {rounds_finished.count(1000)}')
print(f'average game duration: {round(sum(rounds_finished)/300, 2)}')
print(f'Victory percentage by persona')
print([f"{k}: {round((v/len(winners))*100, 2)}" for k, v in winner_count.items()])
print(f'All time winner: {all_time_winner[-1]}')
