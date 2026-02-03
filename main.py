def add (a,b):
    return a+b
def sub (a, b):
    return a-b
def multiply(a,b):
    """Multiply teo numbers."""
    return a*b
def divide (a,b):
    try:
        return a/b
    except ZeroDivisionError:
        print("מה אתה מחלק באפס יא דבע")
