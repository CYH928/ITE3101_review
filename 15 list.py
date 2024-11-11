def ls():
    print(lists)

# -------------------- List --------------------
lists = [95666, 95678, 112907, 60273, 21898, 118973]
# index   [0]    [1]    [2]     [3]    [4]     [5]

print(lists[0]) # display the first item
print(lists[-1]) # display the last one item

print(len(lists)) # list length = 6


lists.append(99999) # append the str/int/float to the last of list
ls()

lists[6] = 33333 # replace which place of the list item
ls()

lists.reverse() # reverse currently order
ls()

# print(sorted(lists))
lists.sort() # sort the list item
ls()

lists.insert(3, 44444) # insert the str/int/float to the list which place
ls()

del lists[3] # delete the list which place item
ls()

lists.remove(33333) # remove the value for the list
ls()

lists += [1, 2, 3] # list + list
# lists = lists + [1, 2, 3]
ls()


# -------------------- String List --------------------
happy = "HAPPY" # set the string variable

for i in happy:
    print(i)


# -------------------- Item in List? --------------------
check = [95666, 999]
for i in check:
    if i in lists: # Check the list have value:95666 or not~
        print("Have " + str(i))
    else:
        print("Don't have " + str(i))