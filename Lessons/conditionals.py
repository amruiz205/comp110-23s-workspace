# """"check lights, if green, says go"""

# light: str = input("What color is the light?") #light is a variable defined as a string that is the answer is to what color is the light
# if (light == "green"): #if this statement is true then print go
#     print("go")
# else: #if its not true, follow the next line of if statements
#     if(light == "yellow"):   #if this is true pring go faster
#         print("go faster")
#     else: #if its not true, go to the next line of statements, ETC.
#         if(light == "red"): #the statement inside the quotations needs to be exactly the same in order to determine if its should print stop
#             print("stop")
#         else:
#             if(light != "red"):
#                 print("i dont know whats going on")
                
# xs: str = "123"
# ys: str = "45"
# x_indx: int = 0
# while x_indx < len(xs):
#     y_indx: int = 0
#     while y_indx < len(ys):
#         print(f"({xs[x_indx]},{ys[y_indx]})")
#         y_indx = y_indx + 1
#     x_indx = x_indx + 1
    


# def mimic(my_words: str) -> str:
#     """given the string my_words, output the same string"""
#     return my_words
# mimic("hello")
# print(mimic("hello"))

# my_words: str = "hello"
# response: str = mimic(my_words)
# print(response)




def mimic(my_words: str, i: int):
    """returns my input"""
    if 1 >= len(my_words):
       return("the lenght of the index is too high, try again")
    return(my_words[i])

mimic(input("choose a word"), input("choose an index"))
print(mimic(input("choose a word"), input("choose an index")))
