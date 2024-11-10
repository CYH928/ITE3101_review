animal = ['cat', 'dog', 'human']

for i in animal:
    print(i)

# loop range
for x in range(6): # loop 6 times, from 0 start 0 to 5, but 6 not included
    print(x)

for x in range(23, 26): # loop from 23 start 23 to 26, but behind the 26 will break down so it will show 23 to 25
    print(x)

for x in range(10, 30, 3): # This loop from 10 start to the 29, when each loop will skip 2 num, like 10, 13, 16
    print(x)

for x in range(30, 10, -3): # This loop from 30 start to the 11, when each loop will skip -2 num, like 30, 27, 24
    print(x)

animal.reverse()
for a in range(len(animal)):
    print(animal[a])