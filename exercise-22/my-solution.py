moves = ['rock', 'paper', 'scissors']
def rpsWinner(move1, move2):
  if move1 == move2: return 'tie'
  if move1 == 'rock' and move2 == 'scissors': return 'player one'
  if move1 == 'paper' and move2 == 'rock': return 'player one'
  if move1 == 'scissors' and move2 == 'paper': return 'player one'
  return 'player two'



assert rpsWinner('rock', 'paper') == 'player two'
assert rpsWinner('rock', 'scissors') == 'player one'
assert rpsWinner('paper', 'scissors') == 'player two'
assert rpsWinner('paper', 'rock') == 'player one'
assert rpsWinner('scissors', 'rock') == 'player two'
assert rpsWinner('scissors', 'paper') == 'player one'
assert rpsWinner('rock', 'rock') == 'tie'
assert rpsWinner('paper', 'paper') == 'tie'
assert rpsWinner('scissors', 'scissors') == 'tie'
print('worked!')