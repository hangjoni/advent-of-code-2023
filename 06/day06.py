from functools import reduce
import operator
import re

with open ('./big_input.txt') as f:
    times_line = f.readline()
    distances_line = f.readline()

    times = list(map(int, re.findall(r'\d+', times_line)))
    distances = list(map(int, re.findall(r'\d+', distances_line)))

    print(times, distances)

# iterate through each race
counts = [] # is a list, store the number of ways we can complete the challenge for that race
for i in range(len(times)):
    time = times[i]
    distance = distances[i]
    count = 0

    # print("Race number: ", i)
    # try each length of time to charge the boat
    for j in range(0, time + 1):
        speed = j
        time_left = time - j
        dist = speed * time_left
        if dist > distance:
            count += 1
            # print("speed: ", speed, "time_left: ", time_left, "dist: ", dist, "distance: ", distance)
    
    # save
    counts.append(count)

# return the results
print(counts)
ways_to_solve = reduce(operator.mul, counts, 1)
print(ways_to_solve)
