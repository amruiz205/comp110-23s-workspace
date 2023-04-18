temp = [
['12-12-2005', 'BMW', '2013', 'buy', '50000'],

 ]       



playing: bool = False
playing_2: bool = True

def calculate_total_bought(x) -> int:
            i: int = 0
            while i < len(temp):
                total_sales = temp[i[4]]
                i += 1
                total_sales = total_sales + temp[i[4]]
            return total_sales


def calculate_total_amount_sold(transactions):
    total_sold = 0
    for transaction in transactions:
        if transaction[3] == 'sell':
            total_sold += int(transaction[4])
    return total_sold

def calculate_annual_sales_by_year(sales_list):
    annual_sales_by_year = {}
    for sale in sales_list:
        year = sale[0].split('-')[2]  
        if year not in annual_sales_by_year:
            annual_sales_by_year[year] = 0
        if sale[3] == 'buy':
            annual_sales_by_year[year] += int(sale[4])
        else:
            annual_sales_by_year[year] -= int(sale[4])
    return annual_sales_by_year

def calculate_vehicles_sold_by_manufacturer(temp):
    vehicles_sold_by_manufacturer = {}
    for transaction in temp:
        manufacturer = transaction[1].lower() 
        transaction_type = transaction[3]
        quantity = int(transaction[4])
        if transaction_type == 'sell':
            if manufacturer in vehicles_sold_by_manufacturer:
                vehicles_sold_by_manufacturer[manufacturer] -= quantity
            else:
                vehicles_sold_by_manufacturer[manufacturer] = -quantity
        else:
            if manufacturer in vehicles_sold_by_manufacturer:
                vehicles_sold_by_manufacturer[manufacturer] += quantity
            else:
                vehicles_sold_by_manufacturer[manufacturer] = quantity
    for manufacturer, quantity in vehicles_sold_by_manufacturer.items():
        if quantity > 0:
            print(f"{manufacturer.capitalize()}: {quantity} vehicles sold")







while playing_2 == True:
    command_options: str = input("MENU:" + "\n" + "--new entry" + "\n" + "--total bought" + "\n" + "--total sold" + "\n" + "--annual sales" + "\n" + "--manufacturers sold" + "\n" + "--transaction history" + "\n" + "--exit" + "\n")
    while command_options != "--new entry" and command_options != "--total bought" and command_options != "--total sold" and command_options != "--annual sales" and command_options != "--manufacturers sold" and command_options !="--exit" and command_options != "--transaction history":
        print("Error: Select a valid option")
    if command_options == "--exit":
        exit()
    if command_options == "--new entry":
        playing_2 = False
        playing = True     
    if command_options == "--transaction history":
        with open('book_keeping.txt', 'r' ) as f:
            print(f.read()) 
    
    if command_options == "--total bought":
        print(calculate_total_bought(temp))
    
    if command_options == "--total sold":
        print(calculate_total_amount_sold(temp))

    if command_options == "--annual sales":
        print(calculate_annual_sales_by_year(temp))
    if command_options == "--manufacturers sold":
        calculate_vehicles_sold_by_manufacturer(temp)
    
    while playing is True:

        transaction_date = input("what day of the month did the transaction took place? ")
        while int(transaction_date) > 31 or int(transaction_date) < 1:
            print("Error: choose a valid date ")
            transaction_date = input("what day of the month did the transaction took place? ")

        
        transaction_month = input("what month the transaction took place? ")
        while int(transaction_month) > 12 or int(transaction_month) < 1:
                print("Error: choose a valid date ")
                transaction_month = input("what month the transaction took place? ")


        transaction_year = input("what year did the transaction take place? ")
        while int(transaction_year) < 1886 or int(transaction_year) > 2027:
                print("Error: choose a valid date ")
                transaction_year = input("what year did the transaction take place? ")

        transaction = transaction_date + "-" + transaction_month + "-" + transaction_year
        l = transaction.split()


        transaction = transaction + " " + input("what was the model? ") 

        model_year = input("what model year is it? ")
        while int(model_year) < 1886 or int(model_year) > 2027:
            print("Error: choose a valid year ")
            model_year = input("what model year is it? ")

        transaction = transaction + " " + model_year

        transaction_type = input("was the transaction a buy or sell? ")
        while (transaction_type != ("sell")) and (transaction_type != ("buy")):
            print("Error: Select a valid transaction type ")
            transaction_type = input("was the transaction a buy or sell? ")



        transaction_price = input("what was the price of the transaction? ")
        while int(transaction_price) < 0:
            print("Error: select a valid price ")
            transaction_price = input("what was the price of the transaction? ")

        transaction = transaction + " " + transaction_type + " " + transaction_price

        l = transaction.split()
        temp.append([l])
  
        with open('book_keeping.txt', 'a') as file:
            file.write("\n" + str(l))
        
        keep_playing: str = input("would you like to put in another transaction? ")
        if keep_playing != ("no") and keep_playing != ("yes"):
            print("Error: Select a valid answer ")
            exit()
        if keep_playing == "no":
            playing = False
            playing_2 = True



