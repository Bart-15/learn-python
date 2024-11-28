import random
import time

teamA_name = 'TeamA'
teamA_rank = 5
teamB_name = 'TeamB'
teamB_rank = 12

teamA_chance = random.randint(0,16)
teamB_chance = random.randint(0,16)

print('The pickalator is now choosing a winner...\n')
time.sleep(2)

print('...almost there...\n')

time.sleep(2)

if teamA_chance >= teamB_chance:
  confidence = (teamA_chance - teamB_chance) / 31 * 100
  print(f'⭐️The Pickalator has choosen: {teamA_name} with {int(confidence)}% confidence⭐️')
else: 
  confidence = (teamB_chance - teamA_chance) / 31 * 100
  print(f'⭐️The Pickalator has choosen: {teamB_name} with {int(confidence)}% confidence⭐️')
