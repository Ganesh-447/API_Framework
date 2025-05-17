def calculator(a,b,operation):

    if operation == 'add':
        return a+b
    elif operation == 'sub':
        return a-b
    elif operation == 'mul':
        return a*b
    elif operation == 'divide':
        if b!=0:
            return a/b
        else:
            return "Cannot divide by zero"
    else:
        return "Invalid Operation"
print(calculator(5,6,'add'))
print(calculator(5,0,'divide'))