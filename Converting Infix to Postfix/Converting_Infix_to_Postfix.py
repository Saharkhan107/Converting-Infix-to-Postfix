def precedence(operator):
    # Return the precedence of operators
    if operator == '+' or operator == '-':
        return 1
    elif operator == '*' or operator == '/':
        return 2
    return 0  # For non-operators

def infix_to_postfix(expression):
    # Initialize an empty stack for operators and an empty list for the output
    stack = []
    output = []

    # Loop through each character in the input expression
    for char in expression:
        if char.isalnum():  # If the character is an operand (A, B, C, etc.)
            output.append(char)
        elif char == '(':  # If the character is '(', push it to the stack
            stack.append(char)
        elif char == ')':  # If the character is ')'
            # Pop from the stack until a '(' is encountered
            while stack and stack[-1] != '(':
                output.append(stack.pop())
            stack.pop()  # Pop '(' from the stack
        else:  # If the character is an operator (+, -, *, /)
            # Pop operators from the stack to the output until the operator at the top of the stack
            # has lower precedence or the stack is empty
            while stack and precedence(stack[-1]) >= precedence(char):
                output.append(stack.pop())
            # Push the current operator to the stack
            stack.append(char)

    # Pop any remaining operators from the stack
    while stack:
        output.append(stack.pop())

    # Return the output list as a string
    return ''.join(output)

# Test cases
print(infix_to_postfix("A*(B+C)"))  # Expected output: "ABC+*"
print(infix_to_postfix("A+B*(C-D)"))  # Expected output: "ABCD-*+"
print(infix_to_postfix("(A+B)*(C-D)"))  # Expected output: "AB+CD-*"
print(infix_to_postfix("A+B*C-D/E"))  # Expected output: "ABC*+DE/-"

