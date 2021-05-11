"""          *       1 = (0 * 2) + 1
            ***      3 = (1 * 2) + 1
           *****     5 = (2 * 2) + 1
          *******    7 = (3 * 2) + 1
         *********   9 = (4 * 2) + 1
"""
userInput = int(input("number pyramid generator : "))
space = userInput
for i in range(userInput):
    print(space * 2 * " "," *" * (i*2+1))
    space -= 1
