def operate(operand0, operand1, operator):
    if operator == "+":
        return str(int(operand0) + int(operand1))
    elif operator == "*":
        return str(int(operand0) * int(operand1))
    elif operator == "-":
        return str(int(operand0) - int(operand1))

if __name__ == "__main__":
    import sys
    expr = sys.stdin.readline().strip().split()
    stack = []
    for t in expr:
        if t.isdigit():
            stack.append(t)
        else:
            a = stack.pop()
            b = stack.pop()
            stack.append(operate(b, a, t))
    print stack.pop()