import re

print("My Magical Calculator")
print("Type 'quit' to exit\n")

previous = None
run = True

def performMath():
    global run
    global previous
    equation = ""
    if previous == None:
        equation = input("Enter equation:")
    else:
        equation = input(str(previous))
    if equation == "quit":
        run = False
    else:
        equation = re.sub('[a-zA-Z,:()" "]', "", equation)

        if previous == None:
            previous = eval(equation)
        else:
            previous = eval(str(previous) + equation)
        print("Result:", previous)

while run:
    performMath()