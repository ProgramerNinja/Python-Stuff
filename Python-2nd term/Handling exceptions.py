##Jared M.
##1/2/2019
##exception handling

while True:
    try:
        num=float(input("Enter a number: "))
    except:
        print("Something went wrong!")
    try:
        print(num)
    except:
        print("nothing to print")


try:
    num = float(input("\nEnter a number: "))
except ValueError:
    print("Thats not a number!")
except ValueError:
    print("Name error!")


for value in (None,"Hi"):
    try:
        print("Attempting to convert" , value, "-->", end=" ")
        print(float(value))
    except (TypeError):
        print("something went wrong! type error")
    except (ValueError):
        print("something went wrong! value error")


try:
    num = float(input("\nEnter a number: "))
except ValueError as e:
    print("That was not a number! Or as Python would say \n" ,e)


try:
    num = float(input("\nEnter a number: "))
except ValueError:
    print("That was not a number!")
else:
    print("you entered the number", num)


print(num)
