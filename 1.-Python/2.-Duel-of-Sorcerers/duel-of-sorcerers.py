#1. Create two variables called gandalf and saruman and assign them the spell power lists. Create a variable called spells to store the number of spells that the sorcerers cast

gandalf = [10, 11, 13, 30, 22, 11, 10, 33, 22, 22]
saruman = [23, 66, 12, 43, 12, 10, 44, 23, 12, 17]

spells = len(gandalf)

#2. Create two variables called gandalf_wins and saruman_wins. Set both of them to 0.

gandalf_wins = 0
saruman_wins = 0

#3. Using the lists of spells of both sorcerers, update variables gandalf_wins and saruman_wins to count the number of times each sorcerer wins a clash.

for i in range(0, spells):
    if gandalf[i] > saruman[i]:
        gandalf_wins += 1
    else:
        saruman_wins += 1

print('Gandalf won:', gandalf_wins, 'clashes')
print('Saruman won:', saruman_wins, 'clashes')

#4. Who won the battle?

if gandalf_wins > saruman_wins:
    print('Gandalf won the battle')
elif gandalf_wins == saruman_wins:
    print('Tie')
else: 
    print('Saruman won the battle') 