def print_formatted(number):
    # your code goes here
    width = len(bin(number)[2:])
    
    print(bin(width))
    # for i in range(number):
    #     print(f"{(i+1):^}", end='')
    #     print(f"{(i+1):^o}", end='')
    #     print(f"{(i+1):^X}", end='')
    #     print(f"{(i+1):^b}", end='')
    #     print()

if __name__ == '__main__':
    n = int(input())
    print_formatted(n)