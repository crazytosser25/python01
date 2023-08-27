result = None
operand = None
operator = None
wait_for_number = True

while True:
   try:
       operand = int(input())
   except ValueError:
       print(f'{operand} is not a number. Try again.')
       operand = int(input())
    if result = None:
        result = operand
    wait_for_number = False
    try:
        operator = input()
        operator = int(operator)
    except ValueError:
        continue
    else:
        print(f'{operator} is not '+' or '-' or '/' or '*'. Try again')
        operator = input()