temp = [
['12-12-2005', 'BMW', '2013', 'buy', '50000']
['12-12-2007', 'honda', '2013', 'sell', '5000']
['12-10-2006', 'hyundai', '2013', 'sell', '500000']
['29-12-2005', 'BMW', '1900', 'buy', '50000']
['12-12-2019', '2024', '2024', 'buy', '60000000']
['12-12-2005', 'bmw', '2005', 'buy', '20000']
['12-12-2005', 'BMW', '2013', 'buy', '20000']
['12-12-2005', 'BMW', '2015', 'buy', '50000']
['12-12-2005', 'BMW', '2005', 'buy', '50000000']
['12-12-2005', 'BMW', '2005', 'buy', '500000']
['12-12-2005', 'BMW', '2013', 'buy', '500000']
['12-12-2005', 'BMW', '2005', 'buy', '2015']
 ]       

# with open('book_keeping.txt') as x:
#     lines = x.readlines()  


playing: bool = False
playing_2: bool = True


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
        print('x')
        # def calculate_total_sales(temp):
        #     i: int = 0 
        #     while i < len(temp):
        #         if temp[i[2]] == year:
        #             total_sales += temp[i[4]]
        #     return total_sales
    
    #    def calculate_total_sales(temp, year): 
    #         total_sales = 0
    #         for i in temp:
    #             if i[2] == year:
    #                 total_sales += i[4]
    #         return total_sales
    # print(calculate_total_sales)  

    
    
    
    
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
            playing_2 = True



# while playing_2 == True:
#     command_options: str = input("OPTIONS:" + "\n" + "--new entry" + "\n" + "--total bought" + "\n" + "--total sold" + "\n" + "--annual sales" + "\n" + "--manufacturers sold" + "\n" + "--exit" + "\n")
#     while command_options != "--new entry" or "--total bought" or "--total sold" or "--annual sales" or "--manufacturers sold" or "--exit":
#         print("Error: Select a valid option")
#     if command_options == "exit":
#         exit()


# with open('book_keeping.txt', 'r' ) as f:
#             print(f.read()) 

# with open('book_keeping.txt', 'r') as l:
#     print(f[4].read())

