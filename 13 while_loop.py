times = 10

while times >= 0:
    print(times) # Friendly remind, four spaces’ indentation indicate a “block” of code.
    times -= 1 # When one time looping -1 times

    if times == 6:
        break
else:
    print("End")