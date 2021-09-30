#pw = times player wins
#cw = times computer Wins
#dr = times they draw
pw = 0
cw = 0
dr = 0
from random import randint
n = int(input('How many rounds would you like? '))
for i in range(1, n, 1):
  print('Round', i)
  player = input('rock (r), paper (p),scissor (s): ')
  print(player, 'vs', end=(' '))
  chosen = randint(1,3)
  if chosen == 1:
    computer = 'r'
  elif chosen == 2:
    computer = 'p'
  else:
    computer = 's'
  print(computer)
  if player == computer:
    print('DRAW')
    dr += 1
  elif player == 'r' and computer == 's':
    print('Player wins')
    pw += 1
  elif player == 'r' and computer == 'p':
    print('Computer wins')
    cw += 1
  elif player == 'p' and computer == 'r':
    print('Player wins')
    pw += 1
  elif player == 'p' and computer == 's':
    print('Computer wins')
    cw += 1
  elif player == 's' and computer == 'p':
    print('Player wins')
    pw += 1
  elif player == 's' and computer == 'r':
    print('Computer wins')
    cw += 1
print('Times player wins:', pw, '\n', 'Times computer wins: ', cw, '\n', 'Times player draws with computer: ', dr)
if pw > cw:
  print('Player wins the game')
elif cw > pw:
  print('Computer wins the game')
else:
  print('It is a DRAW')