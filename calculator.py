def add(a, b):
    return a + b

def sub(a, b):
    return b - a

def div(a, b):
    return a/b

def mult(a, b):
    if not isinstance(a,(int, float)) or not isinstance(b,(int,float)):
        return "Error: Input must be numbers."
    
    return a*b

