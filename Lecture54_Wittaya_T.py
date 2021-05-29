def login():
    username = input("enter your username :")
    password = input("enter your password :")
    if username == "gide" and password == "1234":
        return menu()
    else:
        print("Try again")
        return login()

def menu():
    print("---Calculate Price---")
    print("1. Vat Calculate")
    print("2. Total Price Calculate")
    return menuselect()

def menuselect():
    userselected = int(input("enter your choice : "))
    if userselected == 1:
        price = int(input("enter price :"))
        return vatcal(price)
    elif userselected == 2:
        return pricecal()
    else:
        return menuselect()

def vatcal(totalprice):
    result = totalprice + (totalprice * 7/100)
    return result

def pricecal():
    price1 = int(input("Product price :"))
    price2 = int(input("Product price :"))
    return vatcal(price1+price2)

print(login())