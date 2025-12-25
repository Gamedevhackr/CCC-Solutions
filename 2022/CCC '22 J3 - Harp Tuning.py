# 15/15 do not have to print all outputs at one, can print part by part

x = str(input())

letters = "ABCDEFGHIJKLMNOPQRST"
numbers = "0123456789"

for i in x:
    if i in numbers:
        is_number = True
        print(i, end="")

    elif i not in numbers:

        if i == "+":
            print(" tighten ", end="")
           
        elif i == "-":
            print(" loosen ", end="")
            
    
        elif i in letters:
            print(i, end="")
            
