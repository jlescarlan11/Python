import random

def generate_lottery_numbers(specified_numbers=None):
    while True:
        # Create a pool of numbers
        number_pool = [5, 18, 7, 3, 22, 11, 4, 14, 17, 29, 1, 26, 10, 31, 34, 16, 32, 9, 41, 38, 8, 30, 39, 36, 37, 35, 6, 21]
        number_of_even = random.randint(2, 5)
        number_below_22 = random.randint(1, 5)

        # Include specified numbers if provided
        if specified_numbers:
            number_pool.extend(specified_numbers)
            # Remove duplicates from the number pool
            number_pool = list(set(number_pool))
        
        # Randomly select 3 numbers below 22
        below_22 = random.sample([num for num in number_pool if num < 22], min(number_below_22, len(number_pool)))
        
        # Randomly select 2 numbers 22 and above
        above_22 = random.sample([num for num in number_pool if num >= 22], 5 - min(number_below_22, len(number_pool)))
        
        # Randomly select 1 specified number to be included
        included_number = random.choice(specified_numbers) if specified_numbers else None
        
        # Combine the sets of numbers
        lottery_numbers = below_22 + above_22 + ([included_number] if included_number else [])
        
        # Ensure 4 even and 2 odd numbers
        even_numbers = [num for num in lottery_numbers if num % 2 == 0]
        odd_numbers = [num for num in lottery_numbers if num % 2 != 0]

        # Check the sum and the count of even and odd numbers
        if (75 <= sum(lottery_numbers) <= 165) and (len(even_numbers) == number_of_even and len(odd_numbers) == (6 - number_of_even)):
            # Sort the numbers in ascending order
            lottery_numbers.sort()
            
            # Ensure unique numbers before returning
            if len(set(lottery_numbers)) == 6:
                return lottery_numbers


# Example usage:
            
specified_numbers = [5, 18, 7, 3, 22, 11, 4]  # Example specified numbers
for i in range(101):
    predicted_numbers = generate_lottery_numbers(specified_numbers)
    with open('a.txt', 'a') as file:
        file.write(f"{i}. Predicted Lottery Numbers: {predicted_numbers}\n")
