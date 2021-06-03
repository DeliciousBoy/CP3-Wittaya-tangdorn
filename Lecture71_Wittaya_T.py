menulist = []
pricelist = []

def bill():
    print("Food".center(20,"-"))
    totalprice = 0
    for number in range(len(menulist)):
        print(menulist[number],pricelist[number])
        totalprice += int(pricelist[number])
    print("total",totalprice)

while True:
    menuname = input("please enter Menu:")
    if menuname.lower() == "exit":
        break
    else:
        menuprice = int(input("menu price: "))
        menulist.append(menuname)
        pricelist.append(menuprice)



bill()

