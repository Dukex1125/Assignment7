import random

players_score = {}
players_rollcount = {}

player_name = raw_input('Please enter your name:')
players_score[player_name] = 0
player_count = int(raw_input('Total players to compete? '))

if player_count > 1:
    while len(players_score) < player_count:
        player_name = raw_input('Please enter another name: ')
        players_score[player_name] = 0

else:
    players_score['computer'] = 0

def displayScore(players_score):
    for key, value in players_score.iteritems():
        print '%s has a score of %i.' % (key, value)

displayScore(players_score)



class DiceNumber(object):
    random_int = random.randint(1, 6)


    def diceNumber(self):
        return (self.random_int)

faceNumber = DiceNumber()

for keys, values in players_score.iteritems():
    # players_score[keys] = players_score[keys] + faceNumber.diceNumber()
    while values < 20:
        for keys, values in players_score.iteritems():
            choice = raw_input("Enter r for roll or h for hold: ")
            if choice == 'r':
                faceNumber.diceNumber()
                players_score[keys] += faceNumber.diceNumber()
                displayScore(players_score)
            else:
                displayScore(players_score)
    else:
        print '%s wins the game with a score of %i.'%(players_score[keys], players_score[values])


displayScore(players_score)
