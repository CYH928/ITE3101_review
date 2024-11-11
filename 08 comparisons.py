print(5 < 10) # True
print(5 > 10) # False

# Textual comparisons
print('Cat' < 'cat') # True
print('C' < 'd') # True
print('Dog' < 'cat') # True

# A-Za-z small<big

first = input("first num: ")
second = input("second num: ")

# Six comparisons
if first == second:
    print(first + "=" + second)
if first != second:
    print(first + "≠" + second)
if first < second:
    print(first + "<" + second)
if first > second:
    print(first + ">" + second)
if first <= second:
    print(first + "≤" + second)
if first >= second:
    print(first + "≥" + second)