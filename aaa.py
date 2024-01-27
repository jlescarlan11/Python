def print_rangoli(size):
    import string
    
    # Create a list of alphabet characters
    alphabet = string.ascii_lowercase
    
    # Create the lines of the rangoli
    lines = []
    for i in range(size):
        s = '-'.join(alphabet[size-1:i:-1] + alphabet[i:size])
        lines.append((s.center(size*4-3, '-')))
        print(lines)

if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)