def add(a, b):
    sum = a + b
    
    return sum
  
def sub(a, b):
    diff = a - b
    
    return diff

def div(a, b):
    try:
     return a / b
    except ZeroDivisionError:
        return "You cannot divide a number by zero, sorry :9"

def mult(a, b):
    if not isinstance(a,(int, float)) or not isinstance(b,(int,float)):
        return "Error: Input must be numbers."
    
    return a*b
 
x = int(input("Enter your first value: "))
y = int(input("Enter your first value: "))

print("Your first value is",x, "and your second value is",y)


print("1: Addition")
print("2: Subtraction")
print("3: Division")
print("4: Multiplication")
choice = input("What do operation do you want to do? ")

match choice:
    case "1":
        print(add(x,y))
    case "2":
        print(sub(x,y))
    case "3":
        print(div(x,y))
    case "4":
        print(mult(x,y))

