
while True:
    choice = input("\nWould you like to add, subtract, multiply, divide or exit?: ").lower()

    if choice == "add":
        add_input1 = input("\nWhat is the first number to add?: ")
        add_input2 = input("What is the second number to add?: ")
        if add_input1.isdigit() and add_input2.isdigit():
            add_input1 = int(add_input1)
            add_input2 = int(add_input2)
            add_output = add_input1 + add_input2
            print(f"\n{add_input1} + {add_input2} = {add_output}")
        else:
            print("\nInvalid input. Please input digits.")
    
    elif choice == "subtract":
        subtract_input1 = input("\nWhat is the first number to subtract?: ")
        subtract_input2 = input("What is the second number to subtract?: ")
        if subtract_input1.isdigit() and subtract_input2.isdigit():
            subtract_input1 = int(subtract_input1)
            subtract_input2 = int(subtract_input2)
            subtract_output = subtract_input1 - subtract_input2
            print(f"\n{subtract_input1} - {subtract_input2} = {subtract_output}")
        else:
            print("\nInvalid input. Please input digits.")

    elif choice == "multiply":
        multiply_input1 = input("\nWhat is the first number to multiply?: ")
        multiply_input2 = input("What is the second number to multiply?: ")
        if multiply_input1.isdigit() and multiply_input2.isdigit():
            multiply_input1 = int(multiply_input1)
            multiply_input2 = int(multiply_input2)
            multiply_output = multiply_input1 * multiply_input2
            print(f"\n{multiply_input1} * {multiply_input2} = {multiply_output}")
        else:
            print("\nInvalid input. Please input digits.")

    elif choice == "divide":
        divide_input1 = input("\nWhat is the first number to divide?: ")
        divide_input2 = input("What is the second number to divide?: ")
        if divide_input1.isdigit() and divide_input2.isdigit():
            divide_input1 = int(divide_input1)
            divide_input2 = int(divide_input2)
            if divide_input2 == 0:
                print("\nYou cannot divide by 0.")
            else:
                divide_output = divide_input1 / divide_input2
                print(f"\n{divide_input1} / {divide_input2} = {divide_output}")   
        else:
            print("\nInvalid input. Please input digits.")
    
    elif choice == "exit":
        print("\nGoodbye")
        break

    else:
        print("\nPlease enter a valid action (add, subtract, multiply, divide or exit.")