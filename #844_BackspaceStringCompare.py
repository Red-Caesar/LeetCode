s = "##"
t = "c#d#"
stack_s = []
stack_t = []
for c in s:
    if c != '#':
        stack_s.append(c)
    elif stack_s:
        stack_s.pop()
for c in t:
    if c != '#':
        stack_t.append(c)
    elif stack_t:
        stack_t.pop()
print(stack_s == stack_t)