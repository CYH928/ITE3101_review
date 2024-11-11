n = input("Please input a number:\n")
if n.isdigit():
    print("$" * int(n))  # String + String OR String * Integer
    print("$" * int(n) * 2)
else:
    print("Invalid Number!")


def func(x:int)->int:
    return (x ** 2) + 2(x) + 1

def checking(i:int, j:int)->int:
    count = 0
    while func(i) < j:
        count += 1
    else:
        return count


record = [ # Nested list
    ["Name", "Age", "Location", "Position"],
    ["Judy", "20", "Tai Po", "Clark"],
    ["Tom", "25", "Fanling", "Sales"],
    ["Peter", "18", "Sha Tin", "Programmer"]
]
# print(record[1][0])


record = [ # list of Dictionary
    {'Name':'Judy', 'Age':'20', 'Location':'Tai Po', 'Position':'Clark'},
    {'Name':'Tom', 'Age':'25', 'Location':'Fanling', 'Position':'Sales'},
    {'Name':'Peter', 'Age':'18', 'Location':'Sha Tin', 'Position':'Programmer'}
]
# # print(record[0]['Name'])


# for i in record:
#     if i['Location'] == "Sha Tin":
#         print(i['Name'])