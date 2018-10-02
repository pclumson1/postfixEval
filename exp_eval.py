from stack_array import *


class PostfixFormatException(Exception):
    pass

# Evaluate a postfix expression and return the result
# String -> Float
def postfix_eval(input_str):
    """Takes in an expression in postfix form, evaluates it, and returns the result"""
    op_stack = Stack(30)
    postfix_list = input_str.split()
    test_list = list(postfix_list)
    if len(postfix_list) == 0:
        raise PostfixFormatException("Insufficient operands")
    # Runs through a copy of the list, and checks for anything that is NOT an operand or operator
    for token in test_list:
        if token not in "^*/+-(":
            try:
                float(token)
            except:
                raise PostfixFormatException("Invalid token")
    # Runs through
    for token in postfix_list:
        if token not in "^*/+-(":
            op_stack.push(float(token))
        else:
            if op_stack.size() < 2:
                raise PostfixFormatException("Insufficient operands")
            num1 = float(op_stack.pop())
            num2 = float(op_stack.pop())
            if token == '^':
                op_stack.push(num2 ** num1)
            elif token == '*':
                op_stack.push(num2 * num1)
            elif token == '/':
                if num1 == 0:
                    raise ValueError()
                else:
                    op_stack.push(num2 / num1)
            elif token == '+':
                op_stack.push(num2 + num1)
            elif token == '-':
                op_stack.push(num2 - num1)
    if op_stack.size() != 1:
        raise PostfixFormatException("Too many operands")
    return op_stack.pop()

# Converts an expression written in infix notation to postfix notation
# String -> String
def infix_to_postfix(input_str):
    """Takes in an expression written in the common infix notation and transforms it into an expression
    in the postix notation"""
    precedence = {}
    precedence['^'] = 4
    precedence['*'] = 3
    precedence['/'] = 3
    precedence['+'] = 2
    precedence['-'] = 2
    precedence['('] = 1
    op_stack = Stack(30)
    postfix_list = []
    token_list = input_str.split()
    for token in token_list:
        if token not in "^*/+-()":
            postfix_list.append(token)
        elif token == '(':
            op_stack.push(token)
        elif token == ')':
            while op_stack.peek() != '(':
                postfix_list.append(op_stack.pop())
            op_stack.pop()
        else:
            prec = precedence[token]
            while (not op_stack.is_empty()) and \
                  ((token != "^" and precedence[op_stack.peek()] >= prec) or (precedence[op_stack.peek()] > prec)):
                postfix_list.append(op_stack.pop())
            op_stack.push(token)
    while not op_stack.is_empty():
        postfix_list.append(op_stack.pop())
    return ' '.join(postfix_list)

# Converts prefix expression to postfix expression
# String -> String
def prefix_to_postfix(input_str):
    """Takes in an expression in the slightly less common prefix notation and converts it into the
    postfix notation"""
    token_list = input_str.split()
    token_list.reverse()
    op_stack = Stack(30)
    postfix_list = []
    for token in token_list:
        if token not in "^*/+-()":
            op_stack.push(token)
        else:
            op1 = op_stack.pop()
            op2 = op_stack.pop()
            expression = op1 + ' ' + op2 + ' ' + token
            op_stack.push(expression)
    return op_stack.pop()
