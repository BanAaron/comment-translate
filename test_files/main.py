# function to greet the user
def greeter(name: str):
    print(f"Hello {name}")


# only run if this is the main file
if __name__ == "__main__":
    # asks the user for their name
    print("What is your name?")
    # grabs the user input
    user_intput = input()
    # calls the greeter function using the text provided by the user
    greeter(user_intput)
