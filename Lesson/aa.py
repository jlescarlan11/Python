# Enter your code here. Read input from STDIN. Print output to STDOUT

def print_logo(width):
    
    c = 'H'

    for i in range(width):
        print((c * i).rjust(width - 1) + c + (c * i).ljust(width - 1))
        
    for i in range(width + 1):
        print((c * width).center(width * 2) + (c * width).center(width * 6))
        
    for i in range(width - 2):
        print((c * width * 5).center(width * 6))
        
    for i in range(width + 1):
        print((c * width).center(width * 2) + (c * width).center(width * 6))
        
    for i in range(width):
        print(((c * (width - i - 1)).rjust(width) + c + (c * (width - i - 1)).  ljust(width)).rjust(width * 6))

        
        


if __name__ == '__main__':
    width = int(input())
    
    print_logo(width)

