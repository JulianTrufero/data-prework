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
avg_temperature_C = sum(temperatures_C)/len(temperatures_C)

print('The average temperature is:', avg_temperature_C)

#5. Imagine that there was a sensor failure at 3am and the data for that specific hour was not recorded. How would you estimate the missing value? Replace the current value of the list at 3am for an estimation
def missing_value(i):
    missing_value = temperatures_C[i-1] + ((temperatures_C[i+1] - temperatures_C[i-1])/((i+1) - (i-1))) * (i - (i-1))
    return(missing_value)

temperatures_C.insert(3,missing_value(3))
temperatures_C.pop(4)

print('Temperatures with missing value replacement', temperatures_C)

#6.Bonus: the maintenance staff is from the United States and does not uderstand the international metric system. Help them by converting the temperatures from Celsius to Fahrenheit
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
elif avg_temperature_C > 65:
    print('The cooling system needs to be replaced')

#BONUS
#1. Create a list with the hours where the temperature is greater than 70ºC. Store it in a variable.
excding_temp_hrs = []

for i in range(0, len(temperatures_C)):
    if temperatures_C[i] > 70:
        excding_temp_hrs.append(i)
print('Exceding temperature hours:', excding_temp_hrs)

#2. Check if the list you created in step 1 has more than 4 consecutive hours

if {excding_temp_hrs[1] == excding_temp_hrs[0] + 1 and
    excding_temp_hrs[2] == excding_temp_hrs[1] + 1 and
    excding_temp_hrs[3] == excding_temp_hrs[2] + 1 and 
    excding_temp_hrs[4] == excding_temp_hrs[3] + 1}:
    print('The exceeding temperature list has more than 4 consecutive hours: the cooling system needs to be replaced')
elif max_temperature > 80:
    print('The cooling system needs to be replaced')
elif avg_temperature_C > 65:
    print('The cooling system needs to be replaced')

#4. Find the average value of the temperature lists (ºC and ºF). What is the relation between both average values?
avg_temperature_F = sum(temperatures_F)/len(temperatures_F)

print('The average temperature in Farenheit is:', avg_temperature_F)
print('The average temperature in Farenheit, is a linear transformation of the Celcius one: Avg(F) = 1.8*Avg(C)+32')
#5. Find the standard deviation of the temperature lists (ºC and ºF). What is the relation between both standard deviations?

squared_dev_C = []
for i in temperatures_C:
    i = (i - avg_temperature_C) ** 2
    squared_dev_C.append(i)

standard_dev_C = (sum(squared_dev_C)/len(temperatures_C)) ** (1/2)
print('The standard deviation for the temperature in Celcius is:', standard_dev_C)

squared_dev_F = []
for i in temperatures_F:
    i = (i - avg_temperature_F) ** 2
    squared_dev_F.append(i)

standard_dev_F = (sum(squared_dev_F)/len(temperatures_F)) ** (1/2)
print('The standard deviation for the temperature in Farenheit is:', standard_dev_F)
print('The standard deviations are proportional by a factor of 1.8: SD(F) = 1.8*SD(C)')


