well_height = 125
daily_distance = 30
nightly_distance = 20
snail_position = daily_distance - nightly_distance

days = 0

while days * snail_position < well_height:
    days += 1
    if days * snail_position >= well_height:
        print('The snail needs', days, 'days to escape the well')

#1. How many days does it take for the snail to escape the well?

well_height = 125
advance_cm = [30, 21, 33, 77, 44, 45, 23, 45, 12, 34, 55]
daily_distance = []

for netdistance in advance_cm:
    netdistance -= 20
    daily_distance.append(netdistance)

accumulated_distance = 0
days = 0
while accumulated_distance < well_height and days < len(daily_distance):
    accumulated_distance += daily_distance[days]
    days += 1
print('The snail needs', days, 'days to escape the well')

#2. What is its maximum displacement in one day? And its minimum?

max_displacement = max(daily_distance[:6])
print('Maximum displacement in one day: ', max_displacement)

min_displacement = min(daily_distance[:6])
print('Minimum displacement in one day: ', min_displacement)

#3. What is its average progress? 
avg_progress = sum(daily_distance[:6])/len(daily_distance[:6])
print('The average progress is:', avg_progress) 

#4. What is the standard deviation of its displacement? 

squared_deviations = []

for i in daily_distance[:6]:
    i = (i - avg_progress) ** 2
    squared_deviations.append(i)

standard_deviation = (sum(squared_deviations)/len(squared_deviations)) ** (1/2)

print('The standard deviation for the snails displacement is:', standard_deviation)
    
