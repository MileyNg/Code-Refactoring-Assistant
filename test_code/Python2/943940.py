def f(exp):
    from operator import add, mul
    ops = {"+": add, "-": lambda a, b:b - a, "*": mul}
    stack = []
    def g(s):
        if s in ops:
            stack.append(ops[s](stack.pop(), stack.pop()))
        else:
            stack.append(int(s))
    map(g, exp.split())
    return stack[-1]
print f(raw_input())