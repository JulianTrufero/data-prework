temperatures_C = [33, 66, 65, 0, 59, 60, 62, 64, 70, 76, 80, 81, 80, 83, 90, 79, 61, 53, 50, 49, 53, 48, 45, 39]

#1. Find the minimum temperature of the day and store it in a variable.
min_temperature = min(temperatures_C)
print('The minimun temperature is:', min_temperature)

#2. Find the maximum temperature of the day and store it in a variable
max_temperature = max(temperatures_C)
print('The maximun temperature is:', max_temperature)

#3. Create a list with the temperatures that are greater than or equal to 70ºC. Store it in a variable.
exceeding_temp = []

for i in range(0, len(temperatures_C)):
    if temperatures_C[i] >= 70:
        exceeding_temp.append(temperatures_C[i])

print('The temperatures exceeding 70ºC are:', exceeding_temp)

#4. Find the average temperature of the day and store it in a variable
avg_temperature = sum(temperatures_C)/len(temperatures_C)
print('The average temperature is:', avg_temperature)

#5. Imagine that there was a sensor failure at 3am and the data for that specific hour was not recorded. How would you estimate the missing value? Replace the current value of the list at 3am for an estimation

def missing_value(i):
    missing_value = temperatures_C[i-1] + ((temperatures_C[i+1] - temperatures_C[i-1])/((i+1) - (i-1))) * (i - (i-1))
    return(missing_value)

temperatures_C.insert(3,missing_value(3))
temperatures_C.pop(4)

print('Temperatures with missing value replacement', temperatures_C)
#6.Bonus: the maintenance staff is from the United States and does not understand the international metric system. Help them by converting the temperatures from Celsius to Fahrenheit

temperatures_F = []
for i in range(0, len(temperatures_C)):
    f = (1.8 * temperatures_C[i]) + 32
    temperatures_F.append(f)

print('Farenheit temperatures:', temperatures_F)

#7. Make a decision!
    
if len(exceeding_temp) > 4:
    print('The cooling system needs to be replaced')
elif max_temperature > 80:
    print('The cooling system needs to be replaced')
elif avg_temperature > 65:
    print('The cooling system needs to be replaced')

#BONUS
#1. Create a list with the hours where the temperature is greater than 70ºC. Store it in a variable.
excding_temp_hrs = []
for i in range(0, len(temperatures_C)):
    if temperatures_C[i] > 70:
        excding_temp_hrs.append(i)
print(excding_temp_hrs)

#2. Check if the list you created in step 1 has more than 4 consecutive hours
#3. Make the decision!

if {excding_temp_hrs[1] == excding_temp_hrs[0] + 1 and
    excding_temp_hrs[2] == excding_temp_hrs[1] + 1 and
    excding_temp_hrs[3] == excding_temp_hrs[2] + 1 and 
    excding_temp_hrs[4] == excding_temp_hrs[3] + 1}:
    print('The exceeding temperature list has more than 4 consecutive hours')
    print('The cooling system needs to be replaced')
elif max_temperature > 80:
    print('The cooling system needs to be replaced')
elif avg_temperature > 65:
    print('The cooling system needs to be replaced')






    

