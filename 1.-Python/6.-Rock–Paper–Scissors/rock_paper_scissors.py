#1. Import the choice function of the random module.

import random

#2. Create a list that includes the 3 possible gesture options of the game: 'rock', 'paper' or 'scissors'. Store the list in a variable called gestures

gestures = ['rock', 'paper', 'scissors']

#3. Create a variable called n_rounds to store the maximum number of rounds to play in a game.

n_rounds = int(input("How many rounds you'd like to play?: "))
while (n_rounds % 2) == 0:
    print('The number of rounds must be odd')
    n_rounds = int(input('Please select again the number of rounds:'))

#4. Create a variable called rounds_to_win to store the number of rounds that a player must win to win the game.

rounds_t_win = int((n_rounds/2) + 1)
print(f"You'll need to win {rounds_t_win} rounds to be the winner of the game")

#5. Create two variables to store the number of rounds that the computer and the player have won

cpu_score = []
player_score = []

#6.Define a function that randomly returns one of the 3 gesture options.

cpuchoice = []
def cpuplays():
     cpuplays = random.sample(gestures, k=1)
     cpuchoice.append(cpuplays[0])
     
#7.Define a function that asks the player which is the gesture he/she wants to show.

playerchoice = []
def player():
     player = input("Wich gesture you'd like to show?: ")
     while player not in gestures:
        print('Please choose between rock, paper or scissors:')
        player = input()
     playerchoice.append(player)  

#8.Define a function that checks who won a round.

roundwinner = []
def round_winner(i):
    round_winner = 0
    if cpuchoice[i] == gestures[0]:
        if playerchoice[i] == gestures[1]:
            round_winner += 2
            roundwinner.append(round_winner)
        elif playerchoice[i] == gestures[2]:
            round_winner += 1
            roundwinner.append(round_winner)
        else: 
            round_winner += 0
            roundwinner.append(round_winner)
    elif cpuchoice[i] == gestures[1]:
        if playerchoice[i] == gestures[2]:
            round_winner += 2
            roundwinner.append(round_winner)
        elif playerchoice[i] == gestures[0]:
            round_winner += 1
            roundwinner.append(round_winner)
        else: 
            round_winner += 0
            roundwinner.append(round_winner)
    elif cpuchoice[i] == gestures[2]:
        if playerchoice[i] == gestures[0]:
            round_winner += 2
            roundwinner.append(round_winner)
        elif playerchoice[i] == gestures[1]:
            round_winner += 1
            roundwinner.append(round_winner)
        else: 
            round_winner += 0
            roundwinner.append(round_winner)

#9.Define a function that prints the choice of the computer, the choice of the player and a message that announces who won the current round

def roundcounter(i):
        cpuscore = 0
        playerscore = 0
        print(f'The CPU choice is: {cpuchoice[i]}')
        print(f'Your choice is: {playerchoice[i]}')
        if roundwinner[i] == 1:
            cpuscore +=1
            cpu_score.append(cpuscore)
            print('The winner of the round is the CPU')
        elif roundwinner[i] == 2:
            playerscore += 1
            player_score.append(playerscore)
            print('The winner of the round is the human player')
        else:
            print("It's a tie")

#10. Now it's time to code the execution of the game using the functions and variables you defined above.

for i in range(0, n_rounds):
    cpuplays()
    player()
    round_winner(i)
    roundcounter(i)

while len(cpu_score) < rounds_t_win and len(player_score) < rounds_t_win: 
    for j in range(len(cpuchoice), len(cpuchoice) + 1):
        cpuplays()
        player()
        round_winner(j)
        roundcounter(j)

#11. Print the winner of the game based on who won more rounds

if len(cpu_score) < len(player_score):
    print('THE WINNER OF THE GAME IS YOU')
elif len(cpu_score) > len(player_score):
    print('THE WINNER OF THE GAME IS CPU')
else:
    print('The game is tied')
