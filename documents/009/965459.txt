text = input().split()
print(max(text, key = lambda w: text.count(w)), max(text, key = lambda w: len(w)))