"""
exception = events detected during execution that inturrupt the flow of a program
"""


# numerator = float(input("Enter the numerator: "))
# denominator = float(input("Enter the denominator: "))
# result = numerator / denominator
# print(result)


try:
    numerator = float(input("Enter the numerator: "))
    denominator = float(input("Enter the denominator: "))
    result = numerator / denominator
    # print(result)
except ZeroDivisionError as e:  #   the e here is optional, 
                                #   it is just to tell user what went wrong
    print(e)
    print("You can't divide a numerator by zero!")
except ValueError:
    print("You can't divide with value other than number.")
except Exception:
    print("Something went wrong :(")
else:   #   This one is also optional
        #   This one will only execute if except block didn't ran
    print(result)
# finally:    #   This one will always execute even tho the except block ran
#     print("This will always execute")

    