totalPrice = int(input("Enter your total price :"))
def VatCalculate(totalPrice):
    result = totalPrice+(totalPrice*7/100)
    return result

print(VatCalculate())