'''
The function below checks whether two or more parameters are equal with each
other
'''

def equal(a, b, c):
    a = int(a)
    b = int(b)
    c = int(c)
    if a == b or a == c or b == c:
        return True
    else:
        return False

print(equal(4, 5, 6))
print(equal(5, '5', 6))
print(equal("7", 7, "7"))
