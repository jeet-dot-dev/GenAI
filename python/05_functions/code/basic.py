# # # def printChai(name: str, chai_type: str):
# # #     if not isinstance(name, str) or not isinstance(chai_type, str):
# # #         raise TypeError("Both arguments must be strings")
    
# # # printChai("jeet",5)

# # # def fetch_sales() :
# # #     print("fetching the sales ")

# # # def filter_data ():
# # #     print("filtering data")

# # # def summerising_data():
# # #     print("summerising")    

# # # def generate_report () :
# # #     fetch_sales()
# # #     filter_data()
# # #     summerising_data()
# # #     print("report is ready")

# # # generate_report()

# # # def calculate_bill(cups,price_per_cup):
# # #     return cups*price_per_cup

# # # my_bill = calculate_bill(5,120)

# # # print(f"Your bills is : ${my_bill}")

# # # def add_vat(price,vat):
# # #     return price * (100+vat)/100

# # # orders = [150,100,200]

# # # for  order in orders :
# # #     rate = add_vat(order,2)
# # #     print(rate)
    
# # # def server_chai():
# # #     chai_type="masala"
# # #     print(f"inside{chai_type}")

# # # chai_type="hello"
# # # print(f"outside{chai_type}") 
# # # server_chai()   

# # # def update_order():
# # #     chai_type = "ginger"
# # #     def kitchen():
# # #         nonlocal chai_type
# # #         chai_type = "kesar"
# # #     kitchen()
# # #     print("after calling kitchen",chai_type)

# # # update_order()

# # # chai_type = "Plain"

# # # def updated_chai():
# # #     global chai_type
# # #     chai_type="honey"
# # #     print(chai_type)

# # # updated_chai();

# # def make_chai(tea,milk):
# #     print(tea)

# # make_chai(tea="darjeeling",milk="6")

# # def secialChai(*ing,**extra):   #kwargs
# #     print(ing);
# #     print(extra)

# # secialChai("chineman","Cardmom",sweetner="honey",foam="yes")

# # def chai_orders(order=[]):
# #     order.append("Malasa")
# #     print(order)

# # chai_orders()
# # chai_orders()

# #early return from a func 
# def chai_status(cups):
#     if cups == 0:
#         return "No left"
#     return "chai is ready"

# # return multiple value 
  
# def chai_report():
#     return 10,20;

# sold,rem = chai_report()
# print(sold)

# types of func 
#pure vs impure
#recruisive func
#lambdas(anonymouse func)

# def pure_chai(cups):
#     return cups*10


cart = []

while True:
    input_product = input("Enter your product name (type 'done' to finish): ").lower()
    
    if input_product == "done":
        break
    
    cart.append(input_product)
    print(f"{input_product} added to the cart")

# Final output
print("\n🛒 Your Shopping Cart:")
for item in cart:
    print(f"- {item}")
