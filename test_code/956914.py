from collections import Counter

blood = Counter()
while 1:
    try:
        a, b = raw_input().split(',')
    except EOFError:
        break
    blood[b] += 1
for b in ['A', 'B', 'AB', 'O']:
    print blood[b]