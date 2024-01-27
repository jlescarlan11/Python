"""
nester function calls = function calls inside other function calls
                        innermost function calls are resolve first
                        returned value is used as argument for the next outer function
"""

# num = input("Enter a whole positive number: ")
# num = float(num)
# num = abs(num)
# num = round(num)

# print(num)

print(round(abs(float(input("Enter a whole positive number: ")))))