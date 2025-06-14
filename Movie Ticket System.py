age = int(input(" Enter Your age: "))
is_student = input("Are you a student (YES/NO): ").lower()

qualifies = False

is_student == "yes"
    
ticket_price = 0

if age <= 5:
    ticket_price = 0
    
elif age <= 12:
    ticket_price = 5
    
elif age <65:
    if is_student == "yes":
        ticket_price = 8
    else:
        ticket_price = 10
        
else:
    ticket_price = 6

group_size = int(input("How many tickets are you buying? "))
total_cost = ticket_price * group_size

if group_size >= 5:
    discount = total_cost * 0.10
    total_cost -= discount
    print(f"Group discounts applied : -${discount: .2f}")
    
print("Welcome ")    
print(f"Your ticket price is: $ {ticket_price}")
print("===== Recipt ======")
print(f"Age: {age}")
print(f"Student {'Yes' if is_student == 'yes' else 'no'}")
print(f"Total: $ {total_cost:.2f} ")
    
