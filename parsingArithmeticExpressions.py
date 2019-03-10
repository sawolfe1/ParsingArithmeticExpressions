
def Calculate(expression):
    postfix = ConvertoToPostfix(expression).split(',')
    stack = []
    operators = ["+", "-", "*", "/"]

    for i in postfix:
        if i.isdigit():
            stack.append(i)
        elif i in operators:
            try:
                stack.append(DoMath(i, stack))
            except:
                print("Error: Divison by 0")
                return
                
    print(stack.pop())

def DoMath(operator, stack):
    right = int(stack.pop())
    left = int(stack.pop())

    if operator == "+":
        return left+right
    elif operator == "-":
        return left-right
    elif operator == "*":
        return left*right
    elif operator == "/":
        return left//right

def ConvertoToPostfix(expression):
    stack = []
    buffer = ""
    length = len(expression)

    for i, char in enumerate(expression):
        if char.isdigit():
            buffer += f"{char}"
            j=i+1
            if j<length and expression[j].isdigit():
                continue
            buffer += ","
        elif char == "(":
            stack.append(char)
        elif char == ")":
            while stack:
                val = stack.pop()
                if val == "(":
                    break
                buffer += f"{val},"
        else:
            while stack and GetPrecedence(char, stack[-1]):
                buffer += f"{stack.pop()},"
            stack.append(char)

    while stack:
        buffer += f"{stack.pop()},"
        
    return(buffer.strip(','))


def GetPrecedence(val, topOfStack):
    precedence = {"+" : 0, "-" : 0, "*" : 1, "/" : 1}

    try:
        return precedence[val]<=precedence[topOfStack]
    except KeyError:
        return False

while True:
    expression = input('Enter an arithmetic expression as a string: ')
    Calculate(expression)