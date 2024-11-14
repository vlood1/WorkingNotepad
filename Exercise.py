colour = "green"

def inside():
    global colour
    colour = "red"
    print(f"The colour inside the function is {colour}.")

print(f"The colour outside the function is {colour}.")

inside()

print(f"The colour outside the function is {colour}.")  
