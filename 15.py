__author__ = 'roan'

import calendar


# Find leap year, and need match '1xx6' pattern
leap_list = []
for year in range(1006, 1996, 10):
    if calendar.isleap(year):
        # <!-- he ain't the youngest, he is the second -->
        if calendar.weekday(year, 1, 27) == 1:  # Monday: 0 Thuesday: 1
            # print(year)
            leap_list.append(year)

print(leap_list[-2])  # <!-- he ain't the youngest, he is the second -->
