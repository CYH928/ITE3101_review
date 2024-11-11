number = int(input("num: "))

# if number % 2 == 0:
#     print('Even')
# else:
#     print('Odd')

if number > 10:
    print('more than 10')
elif number == 5:
    exit() # exit for the if else
    print('equal 5')
elif number < 0:
    print('less than 0')
else:
    print('0-4, 6-10')