""""check lights, if green, says go"""

light: str = input("What color is the light?") #light is a variable defined as a string that is the answer is to what color is the light
if (light == "green"): #if this statement is true then print go
    print("go")
else: #if its not true, follow the next line of if statements
    if(light == "yellow"):   #if this is true pring go faster
        print("go faster")
    else: #if its not true, go to the next line of statements, ETC.
        if(light == "red"): #the statement inside the quotations needs to be exactly the same in order to determine if its should print stop
            print("stop")
        else:
            if(light != "red"):
                print("i dont know whats going on")
                
           
    