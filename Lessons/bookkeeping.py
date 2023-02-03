

transaction_date = input("what day of the month did the transaction took place? ")
if int(transaction_date) > 31 or int(transaction_date) < 1:
    print("Error: choose a valid date ")
    exit()

   
transaction_month = input("what month the transaction took place? ")
if int(transaction_month) > 12 or int(transaction_month) < 1:
        print("Error: choose a valid date ")
        exit()


transaction_year = input("what year did the transaction take place? ")
if int(transaction_year) < 1886 or int(transaction_year) > 2027:
        print("Error: choose a valid date ")
        exit()

transaction = transaction_date + "-" + transaction_month + "-" + transaction_year
list = transaction.split()


transaction = transaction + " " + input("what was the model? ") 

model_year = input("what model year is it? ")
if int(model_year) < 1886 or int(model_year) > 2027:
    print("Error: choose a valid year ")
    exit()

transaction = transaction + " " + model_year

transaction_type = input("was the transaction a buy or sell? ")
if (transaction_type != ("sell")) and (transaction_type != ("buy")):
    print("Error: Select a valid transaction type ")
    exit()



transaction_price = input("what was the price of the transaction? ")
if int(transaction_price) < 0:
    print("Error: select a valid price ")
    exit()

transaction = transaction + " " + transaction_type + " " + transaction_price

list = transaction.split()


with open('book_keeping.txt', 'a') as file:
    file.write("\n" + str(list))
 




