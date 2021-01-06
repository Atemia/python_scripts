# instagram code qick qiz
def mangle(x):
    c = "python"
    x = x[::-1]
    x.upper()
    x = c+x
    if len(x) > 10:
        return x
    else:
        return c
print(mangle('python'))
