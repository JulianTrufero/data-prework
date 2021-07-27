#BONUS
#1. Create two variables called gandalf and saruman and assign them the spell power lists. Create a variable called spells to store the number of spells that the sorcerers cast

powers = {
    'Fireball': 50, 
    'Lightning bolt': 40, 
    'Magic arrow': 10, 
    'Black Tentacles': 25, 
    'Contagion': 45
}

gandalf = ['Fireball', 'Lightning bolt', 'Lightning bolt', 'Magic arrow', 'Fireball', 
           'Magic arrow', 'Lightning bolt', 'Fireball', 'Fireball', 'Fireball']
saruman = ['Contagion', 'Contagion', 'Black Tentacles', 'Fireball', 'Black Tentacles', 
           'Lightning bolt', 'Magic arrow', 'Contagion', 'Magic arrow', 'Magic arrow']
           
spells = len(gandalf)

#2. Create two variables called gandalf_wins and saruman_wins. Set both of them to 0.
gandalf_wins = 0
saruman_wins = 0

#3. Create two variables called gandalf_power and saruman_power to store the list of spell powers of each sorcerer.

gandalf_powers = [] 
saruman_powers = []

#4. The battle starts! Using the variables you've created above, code the execution of spell clashes. Remember that a sorcerer wins if he succeeds in winning 3 spell clashes in a row

for i in range(0, spells):
    if gandalf[i] == 'Fireball':
        gandalf_powers.append(50)
    
    elif gandalf[i] == 'Lightning bolt':
        gandalf_powers.append(40)
    
    elif gandalf[i] == 'Magic arrow':
        gandalf_powers.append(10)

    elif gandalf[i] == 'Black Tentacles':
        gandalf_powers.append(25)

    elif gandalf[i] == 'Contagion':
        gandalf_powers.append(45)

for i in range(0, spells):
    if saruman[i] == 'Fireball':
        saruman_powers.append(50)

    elif saruman[i] == 'Lightning bolt':
        saruman_powers.append(40)
    
    elif saruman[i] == 'Magic arrow':
        saruman_powers.append(10)

    elif saruman[i] == 'Black Tentacles':
        saruman_powers.append(25)

    elif saruman[i] == 'Contagion' :
        saruman_powers.append(45)
    
clash_counter = []

for k in range(0, len(gandalf_powers)):
    if gandalf_powers[k] > saruman_powers[k]:
        clash_counter.append('G')
    else:
        clash_counter.append('S') 

print('Clash winners', clash_counter)

battle = []

for j in range(len(clash_counter) - 2):
    if clash_counter[j] == clash_counter[j+1] and clash_counter[j+1] == clash_counter[j+2]:
        battle.append(clash_counter[j])

if battle[0] == 'G':
    gandalf_wins += 1
    print('Gandalf won 3 clashes in a row')
elif battle[0] == 'S':
    saruman_wins += 1
    print('Saruman won 3 clashes in a row')

if gandalf_wins > saruman_wins:
    print('Gandalf won the battle')

elif gandalf_wins == saruman_wins:
    print('Tie')
    
else: 
    print('Saruman won the battle') 

#5. Find the average spell power of Gandalf and Saruman.

avg_power_gandalf = sum(gandalf_powers)/len(gandalf_powers)

avg_power_saruman = sum(saruman_powers)/len(saruman_powers)

print('The average power of gandalf is: ',avg_power_gandalf)
print('The average power of saruman is: ',avg_power_saruman)

#6.Find the standard deviation of the spell power of Gandalf and Saruman

squared_deviations_gandalf= []

for i in gandalf_powers:
    i = (i - avg_power_gandalf) ** 2
    squared_deviations_gandalf.append(i)

standard_deviation_gandalf = (sum(squared_deviations_gandalf)/len(squared_deviations_gandalf)) ** (1/2)

print('The standardeviation for gandalf is: ',standard_deviation_gandalf)

squared_deviations_saruman = []

for i in saruman_powers:
    i = (i - avg_power_saruman) ** 2
    squared_deviations_saruman.append(i)

standard_deviation_saruman = (sum(squared_deviations_saruman)/len(squared_deviations_saruman)) ** (1/2)

print('The standar deviation for sauman is: ', standard_deviation_saruman)