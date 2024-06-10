ops = {"+": lambda a, b: b + a,
       "-": lambda a, b: b - a,
       "*": lambda a, b: b * a}
def f(stack, s):
    if s in ops:
        stack.append(ops[s](stack.pop(), stack.pop()))
    else:
        stack.append(int(s))
    return stack

print reduce(f, raw_input().split(), [])[-1]
    