fav_games = ['Mario 64', 'Worms', 'Crash Bandicot']

for game in fav_games:
  print(game)

# fav_games.append('Paper game')
fav_games.insert(1, 'Paper game')

# Delete
del(fav_games[2])

print(len(fav_games))
print(fav_games)