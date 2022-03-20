s = input("Text = ")


def capitalize_nth(s, n):
    return s[:n] + s[n:].capitalize()


i = 0
while i < len(s):
    if(s[i] == ' '):
        i += 1
    if(i % 2 == 1):
        s = capitalize_nth(s, i)
    i += 1
else:
    print("New Text =",   s)
