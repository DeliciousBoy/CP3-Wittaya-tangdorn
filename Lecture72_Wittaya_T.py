menulist = []

def bill():
    print("Food".center(20,"-"))
    for number in range(len(menulist)):
        print(menulist[number][0], menulist[number][1])

while True:
    menuname = input("please enter Menu:")
    if menuname.lower() == "exit":
        break
    else:
        menuprice = input("menu price: ")
        menulist.append([menuname, menuprice])

bill()

