# """ask user for number, give hints about number if wrong"""

# secret: int = 10
# guess: int = int(input("guess a number "))

# playing: bool = True

# while playing:
#     if guess == secret:
#         print("correct ")
#         playing = False
#     else:
#         if guess % 2 == 1:
#             print("your guess is odd. the answer is even ")
        
#         if guess < secret:
#             print("Too low ")
        
#         else:
#             print("too high")
#         guess = int(input("wrong guess try again"))





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


# summed_value = 0
# for i in temp:
#     summed_value = summed_value +i[4]
    
# print(summed_value)


#how to define functions
def calculate_total_sales(temp, year):
    """
    #this function adds all 'buy'transactions for a given year.
    args
    ----
    #data: a list of transaction records.
    #year: is year to compute
    returns
    -----
    total_sales: total sales for a given year.
    """
    total_sales = 0
    #for i in temp:
        #if i[2] == year:
            #total_sales += i[4]
    #return total_sales
    i: int = 0 
    while i < len(temp):
        if temp[i[2]] == year:
            total_sales += temp[i[4]]
    return total_sales

while True:
     curr_year = input("give me a yeaar: ")
     print("%f" % calculate_total_sales(data=temp, year=int(curr_year)))

#string formating/string interpelation or f strings
#read file in the beginning of bookkeeping.py to store it in memory

FILE_PATH = "/path/to/file.txt"
temp = read_file(FILE_PATH)



# x = float(x)
# y = 0.5 * x + 1.0 
# return y

# y = dummy_function(2.0)
# print(y)




# while True:
#     z = input("give me a yeaar: ")
#     print("%f" % dummy_function(year=year))









    








