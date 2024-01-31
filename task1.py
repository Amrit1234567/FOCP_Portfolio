def get_order():
    print("Please enter a positive integer!")
    while True:
        try:
            no = int(input("How many pizzas ordered? "))
            return no if no >=1 else get_order()
            
        except ValueError:
            print("Please Enter a number!")

def set_flag(msg):
    arr = ['y','yes','n','no']
    while True:
        data = input(msg)
        if data.lower() in arr:
            if data[0].lower()=="y":
                return True
            elif data[0].lower()=="n":
                return False
        else:
            print("Enter 'y' or 'n'")
            
if __name__ == "__main__":
    total_price = 12
    delivery_cost = 2.5
    flags = {}

    flagname = ("delivery", "tuesday", "app")
    questions = ("Is delivery required?", "Is it Tuesday? ", "Did the customer use the app? ")
    
    
    order = get_order()
    
    flags = {i:set_flag(j) for i, j in zip(flagname, questions)}

    if order>=5 or not flags["delivery"]:
        delivery_cost = 0
    if flags["tuesday"]:
        total_price *= 0.5
    total_price = total_price * order + delivery_cost
    if flags["app"]:
        total_price = total_price * 0.75
    
    print(f"Total Price: £{total_price:.2f}")