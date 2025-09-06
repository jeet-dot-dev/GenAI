# #1 User Role Check 
# role = input("Enter your role : ").lower();

# if role=="admin":
#     print("full access");
# elif role=="editor":
#     print("edit only");
# else :
#     print("unknown role")

# #2 Discount Applicator 

# bill_amount = float(input("Enter your bill amount :"));

# if bill_amount > 1000 :
#     discount = bill_amount * 20 /100 ;
#     print(f"your discount is ${discount}");
# elif bill_amount<1000 and bill_amount>500 : 
#     discount = bill_amount * 10 /100 ;
#     print(f"your discount is ${discount}");
# else :
#     print("no discount")


# Login Attempt System
# correct_pass = "python123"
# max_attempts = 3

# for attempt in range(1, max_attempts + 1):
#     entered_pass = input(f"Enter the password (attempt {attempt}/{max_attempts}): ")
    
#     if entered_pass == correct_pass:
#         print("Login Successful ✅")
#         break
#     else:
#         print("Sorry! Password is incorrect, try again.")
# else:
#     print("Account Locked 🔒")


# Skip Suspicious Orders 
order_amounts = [250,-10,700,0,1200]

for amount in order_amounts :
    if amount <= 0 :
        continue ;
    else :
        print(f"Processing order {amount}")
