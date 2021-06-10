class Customer:
    name = ""
    lastName = ""
    age = 0

    def addCart(self):
        print("Added product to ",self.name,self.lastName,"'s cart")

customer1 = Customer()
customer1.name = "Oat"
customer1.lastName = "Nahi"
customer1.age = 19
customer1.addCart()

customer2 = Customer()
customer2.name = "Poom"
customer2.lastName = "Halak"
customer2.age = 18
customer2.addCart()

customer3 = Customer()
customer3.name = "Bill"
customer3.lastName = "Chobhi"
customer3.age = 19
customer3.addCart()