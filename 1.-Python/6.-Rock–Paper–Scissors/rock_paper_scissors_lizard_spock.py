import random

gestures = ['rock', 'paper', 'scissors', 'lizard', 'spock']


n_rounds = int(input("How many rounds you'd like to play?: "))
while (n_rounds % 2) == 0:
    print('The number of rounds must be odd')
    n_rounds = int(input('Please select again the number of rounds:'))

rounds_t_win = int((n_rounds/2) + 1)
print(f"You'll need to win {rounds_t_win} rounds to be the winner of the game")

cpu_score = []
player_score = []

cpuchoice = []
def cpuplays():
     cpuplays = random.sample(gestures, k=1)
     cpuchoice.append(cpuplays[0])
     
playerchoice = []
def player():
     player = input("Wich gesture you'd like to show?: ")
     while player not in gestures:
        print('Please choose between rock, paper, scissors, lizard or spock:')
        player = input()
     playerchoice.append(player)  


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
        elif playerchoice[i] == gestures[3]:
            round_winner += 1
            roundwinner.append(round_winner)
        elif playerchoice[i] == gestures[4]:
            round_winner += 2
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
        elif playerchoice[i] == gestures[3]:
            round_winner += 2
            roundwinner.append(round_winner)
        elif playerchoice[i] == gestures[4]:
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
        elif playerchoice[i] == gestures[3]:
            round_winner += 1
            roundwinner.append(round_winner)
        elif playerchoice[i] == gestures[4]:
            round_winner += 2
            roundwinner.append(round_winner)
        else: 
            round_winner += 0
            roundwinner.append(round_winner)
    elif cpuchoice[i] == gestures[3]:
        if playerchoice[i] == gestures[0]:
            round_winner += 2
            roundwinner.append(round_winner)
        elif playerchoice[i] == gestures[1]:
            round_winner += 1
            roundwinner.append(round_winner)
        elif playerchoice[i] == gestures[2]:
            round_winner += 2
            roundwinner.append(round_winner)
        elif playerchoice[i] == gestures[4]:
            round_winner += 1
            roundwinner.append(round_winner)
        else: 
            round_winner += 0
            roundwinner.append(round_winner)
    elif cpuchoice[i] == gestures[4]:
        if playerchoice[i] == gestures[0]:
            round_winner += 1
            roundwinner.append(round_winner)
        elif playerchoice[i] == gestures[1]:
            round_winner += 2
            roundwinner.append(round_winner)
        elif playerchoice[i] == gestures[2]:
            round_winner += 1
            roundwinner.append(round_winner)
        elif playerchoice[i] == gestures[3]:
            round_winner += 2
            roundwinner.append(round_winner)           
        else: 
            round_winner += 0
            roundwinner.append(round_winner)

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

if len(cpu_score) < len(player_score):
    print('THE WINNER OF THE GAME IS YOU')
elif len(cpu_score) > len(player_score):
    print('THE WINNER OF THE GAME IS CPU')
else:
    print('The game is tied')
