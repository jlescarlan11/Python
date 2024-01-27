import os

def save_numbers(numbers):
    with open("saved_numbers.txt", "w") as file:
        for number in numbers:
            file.write(f"{number}\n")

def load_numbers():
    numbers = []
    if os.path.exists("saved_numbers.txt"):
        with open("saved_numbers.txt", "r") as file:
            for line in file:
                numbers.append(float(line.strip()))
    return numbers

def main():
    numbers = load_numbers()

    while True:
        user_input = input("Enter a number (or 'done' to finish): ")

        if user_input.lower() == 'done':
            break

        try:
            number = float(user_input)
            numbers.append(number)
        except ValueError:
            print("Invalid input. Please enter a valid number or 'done' to finish.")

    save_numbers(numbers)

    print("\nFrequency of each number (sorted in descending order):")
    frequency_list = get_frequency(numbers)
    for num, freq in frequency_list:
        print(f"{num}: {freq} times")

def get_frequency(numbers):
    frequency_dict = {}
    for number in numbers:
        if number in frequency_dict: 
            frequency_dict[number] += 1
        else:
            frequency_dict[number] = 1
    
    # Sort the frequency dictionary by values in descending order
    sorted_frequency = sorted(frequency_dict.items(), key=lambda x: x[1], reverse=True)
    
    return sorted_frequency

if __name__ == "__main__":
    main()
