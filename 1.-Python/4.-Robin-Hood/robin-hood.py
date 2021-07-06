#1. Robin Hood is famous for hitting an arrow with another arrow. Find the coordinates of the points where an arrow hits another arrow.

points = [(4, 5), (-0, 2), (4, 7), (1, -3), (3, -2), (4, 5), (3, 2), (5, 7), (-5, 7), (2, 2), (-4, 5), (0, -2),
          (-4, 7), (-1, 3), (-3, 2), (-4, -5), (-3, 2), (5, 7), (5, 7), (2, 2), (9, 9), (-8, -9)]

equal_pts = []
for i in range(0, (len(points) - 1)):
    for j in range(i+1 , len(points)):
        if points[i][0] == points[j][0] and points[i][1] == points[j][1]:
            equal_pts.append(points[i])          
     
print('Points where an arrow hits another arrow:', list(set(equal_pts)))

#2. Calculate how many arrows have fallen in each quadrant.

quad1 = []
quad2 = []
quad3 = []
quad4 = []

for i in range(0, len(points)):
    if points[i][0] > 0 and points[i][1] > 0:
        quad1.append(points[i])
    elif points[i][0] < 0 and points[i][1] > 0:
        quad2.append(points[i])
    elif points[i][0] < 0 and points[i][1] < 0:
        quad3.append(points[i])
    elif points[i][0] > 0 and points[i][1] < 0:
        quad4.append(points[i])
    
print('In Q1 have fallen:', len(quad1), 'arrows') 
print('In Q2 have fallen:', len(quad2), 'arrows') 
print('In Q3 have fallen:', len(quad3), 'arrows') 
print('In Q4 have fallen:', len(quad4), 'arrows') 

#3. Find the point closest to the center. Calculate its distance to the center.

def eucldist(x1, y1,x2, y2):
    eucldist = (((x2 - x1) ** 2) + ((y2 - y1) ** 2)) ** (1/2)
    return (eucldist)

distances = []

for i in range(0, len(points)):
    distance = eucldist(0, 0, points[i][0], points[i][1])
    distances.append(distance)

closest = []

for i in range(0, len(points)):
    if eucldist(0, 0, points[i][0], points[i][1]) == min(distances):   
        closest.append(points[i])    

print('The points closer to the center are:', closest)

#4. If the archery target has a radius of 9, calculate the number of arrows that won't hit the target.

out_of_target = []
for i in range(0, len(points)):
    if distances[i] > 9:       
        out_of_target.append(points[i])

print('The points', out_of_target,'will not hit the target')