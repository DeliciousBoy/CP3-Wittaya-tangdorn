def login():
    print("Please enter your username and password")
    usernameInput = input("enter your username here :")
    passwordInput = input("enter your password : ")
    if usernameInput == "gide" and passwordInput == "gide":
        return True
BasicCat = 500
SexsylegsCat = 2500
KungfuCat = 4500
print("Please enter your username and password")
usernameInput = input("enter your username here :")
passwordInput = input("enter your password : ")
if usernameInput == "gide" and passwordInput == "gide":
    print("---Welcome to MeowMawShop---")
    print("-Cat list--")
    print("1. Basic Cat ",BasicCat,"THB","\n"
          +"2. Sexsylegs Cat",SexsylegsCat,"THB","\n"
          +"3. KungFu Cat",KungfuCat,"THB")
    print("Waht type of cat do u wanna buy?")
    typeInput = (input("enter your code :"))
    if typeInput == "1":
        Cat = "BasicCat"
        Number = int(input("u amount >>"))
        totalprice = Number * BasicCat
    elif typeInput == "2":
        Cat = "SecxsylegsCat"
        Number = int(input("u amount >>"))
        totalprice = Number * SexsylegsCat
    elif typeInput == "3":
        Cat = "KungfuCat"
        Number = int(input("u amount >>"))
        totalprice = Number * KungfuCat
    print("amount: ",Number,"total: ",totalprice)
print("------------------Nice Bussiness!!----------------")





login()


