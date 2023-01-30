#change input to a list using split function. store that list as a file.

transaction_date = input("what was the date of the month did the transaction took place? ")
if int(transaction_date) > 31 or int(transaction_date) < 1:
    print("Error: choose a valid date ")
    exit()

   
transaction_month = input("what was the month the transaction took place? ")
if int(transaction_month) > 12 or int(transaction_month) < 1:
        print("Error: choose a valid date ")
        exit()


transaction_year = input("what year did the transaction take place?")
if int(transaction_year) < 1886 or int(transaction_year) > 2027:
        print("Error: choose a valid date ")
        exit()

transaction = transaction_date + "-" + transaction_month + "-" + transaction_year
list = transaction.split()


transaction = transaction + " " + input("what was the model? ") 

model_year = input("what model year is it? ")
if int(model_year) < 1886 or int(model_year) > 2027:
    print("Error: choose a valid year")
    exit()

transaction = transaction + " " + model_year

transaction_type = input("was the transaction a buy or sell? ")
if (transaction_type != ("sell")) and (transaction_type != ("buy")):
    print("Error: Select a valid transaction type")
    exit()



transaction_price = input("what was the price of the transaction? ")
if int(transaction_price) < 0:
    print("Error: select a valid price")
    exit()

transaction = transaction + " " + transaction_type + " " + transaction_price

list = transaction.split()

print(list)
with open('book_keeping.txt', 'a') as file:
    file.write(str(list))

with open('temp.txt', 'r') as file:
    file.write(str(list))






#fruits: str = ["apples", "bananas", "frogs"]
#for x in fruits:
#    print(x)
#    if x == "bananas":
#        break





    
