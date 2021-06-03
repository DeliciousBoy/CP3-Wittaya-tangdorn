menulist = []

def bill():
    print("Food".center(20,"-"))
    total = 0
    for number in range(len(menulist)):
        print(menulist[number][0], menulist[number][1])
        total += int(menulist[number][1])
    print(total)

while True:
    menuname = input("please enter Menu:")
    if menuname.lower() == "exit":
        break
    else:
        menuprice = int(input("menu price: "))
        menulist.append([menuname, menuprice])


bill()

