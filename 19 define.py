from typing import List

animal = ['cat', 'dog', 'human']

def func(p:List[str])->str: # define the function called func with parameter p list in string, and return string.
    for i in p:
        print(i)

func(animal)

# end of P.320