#1. Calculate the number of stops.
stops = [(10, 0), (4, 1), (3, 5), (3, 4), (5, 1), (1, 5), (5, 8), (4, 6), (2, 3)]
num_stops = len(stops)

#2. Assign to a variable a list whose elements are the number of passengers at each stop (in-out)

passengers_lst = []
passengers = 0

for i in range(0, num_stops):
    passengers += stops[i][0] - stops[i][1]
    passengers_lst.append(passengers)

print(passengers_lst)

#3. Find the maximum occupation of the bus.

max_occupation = max(passengers_lst)
print('The maximum occupation of the bus is:', max_occupation)

#4. Calculate the average occupation. And the standard deviation.

avg_ocuppation = sum(passengers_lst)/len(passengers_lst)
print('The average occupation of the bus is:', avg_ocuppation)

squared_deviations = []
for i in passengers_lst:
    i = (i - avg_ocuppation) ** 2
    squared_deviations.append(i)

stddev_occupation = (sum(squared_deviations )/len(squared_deviations )) ** (1/2)
print('The standard deviation for the bus occupation is:', stddev_occupation)