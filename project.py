total = 0
customer_queue = []

while True:
    customer_name = input("Enter customer name (or 'q' to quit): ")
    
    if customer_name.lower() == 'q':
        break 
    
    customer_total = 0
    
    while True:
        item = input("Enter the item name (or 'done' to finish): ")
        
        if item.lower() == 'done':
            break 
        
        try:
            quantity = int(input("Enter the quantity of {}:".format(item)))
            price_per_item = float(input("Enter the price per {}:".format(item)))
        except ValueError:
            print("Invalid input. Please enter a valid quantity and price.")
            continue 
        
       
        item_cost = quantity * price_per_item
        
        
        customer_total += item_cost
    
   
    total += customer_total
    
    
    print("Customer: {}".format(customer_name))
    print("Total: ${:.2f}".format(customer_total))
    
    
    new_customer = input("Go to the next customer (Y/N): ").lower()
    
    if new_customer != 'y':
        break  

print("Overall Total: ${:.2f}".format(total))
