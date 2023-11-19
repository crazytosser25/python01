result = None
operand = None
operator = None
wait_for_number = True

while True:
    input_value = input()

    if input_value == "=":
        print(result)
        break

    if wait_for_number:
        try:
            input_value = int(input_value)
        except ValueError:
            print(f'{operand} is not a number. Try again.')
            input_value = int(input())
        if result:
            operand = input_value
        else:
            result = input_value

        wait_for_number = False
    
    else:
        try:
            input_value = int(input_value)
        except ValueError:
            operator = input_value
        else:
            print(f"{operator} is not '+' or '-' or '/' or '*'. Try again.")
            operator = input()

        wait_for_number = True

    if result and operand and operator and wait_for_number == False:
        if operator == '+':
            result += operand
        elif operator == '-':
            result -= operand
        elif operator == '*':
            result *= operand
        elif operator == '/':
            result /= operand

        
        