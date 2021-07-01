well_height = 125
daily_distance = 30
nightly_distance = 20
snail_position = daily_distance - nightly_distance

days = 0

while days * snail_position < well_height:
    days += 1
    if days * snail_position >= well_height:
        print('The snail needs', days, 'days to escape the well')

    
    
