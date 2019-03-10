

expression = input('Enter an arithmetic expression as a string: ')
Calculate(expression)

def Calculate(expression):

    stack = []
    buffer = ""
    operators = ["+", "-", "/", "*"]
    for i in expression:
        if i.isdigit():
            buffer += f"{i}"
        elif i == "(":
            stack.append(i)
        elif i == ")":
            while stack and stack[-1] != "(":
                val = stack.pop()
                buffer += f"{val}"
        else:
            while stack and GetPrecedence(i, stack):
                buffer += f"{stack.pop()}"
            stack.append(i)

    while stack:
        buffer += f"{stack.pop()}"
        
    print(buffer)


def GetPrecedence(val, stack):
    precedence = {'+':1, '-':1, '*':2, '/':2}

    try:
        a = precedence[val]
        b = precedence[stack[-1]]
        return a<=b
    except KeyError:
        return False