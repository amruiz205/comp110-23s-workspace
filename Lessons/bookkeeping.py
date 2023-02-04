playing: bool = True
playing_2: bool = True
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
    list = transaction.split()


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

    list = transaction.split()

    with open('book_keeping.txt', 'a') as file:
        file.write("\n" + str(list))

    keep_playing: str = input("would you like to put in another transaction? ")
    if keep_playing != ("no") and keep_playing != ("yes"):
        print("Error: Select a valid answer ")
        exit()
    if keep_playing == "no":
        playing = False

# with open('book_keeping.txt', 'r' ) as f:
#     print(f.read()) 


while playing_2 == True:
    command_options: str = input("OPTIONS:" + "\n" + "--total bought" + "\n" + "--total sold" + "\n" + "--annual sales" + "\n" + "--manufacturers sold" + "\n" + "--exit" + "\n")
    




