while True: 
    try:
        a = input("Calculation: ") 
        result = eval(a)
        print(f"Answer: {result}") 
    except (SyntaxError, NameError, ZeroDivisionError) as e: 
        print(f"Error: {e}") 
    except Exception as e: 
        print(f"An unexpected error occurred: {e}") 