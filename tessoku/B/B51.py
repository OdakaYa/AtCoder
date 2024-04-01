S = input()

stack = []
for i, s in enumerate(S):
  if s == "(":
    stack.append([i+1, s])
  else:
    l = stack.pop()
    print(l[0], i+1)