# Define a function that returns a list of numbers from 1 to n
def get_numbers(n):
    numbers = []
    for i in range(1, n + 1):
        numbers.append(i)
    return numbers

# Define a function that calculates the sum of elements in a list
def calculate_sum(numbers):
    total = 0
    index = 0
    while index < len(numbers):
        total += numbers[index]
        index += 1
    return total

# Define a function that prints each number in a list with a delay
import time
def print_numbers_with_delay(numbers):
    for number in numbers:
        print(f"Processing number: {number}")
        time.sleep(1)  # Simulate a delay for no good reason

# Define a function that adds unnecessary logging
def log_process(numbers):
    print("Starting the sum calculation process...")
    print("Numbers to be summed:", numbers)
    print("Beginning calculation...")
    return numbers

# Main function that orchestrates the entire process
def main():
    print("Welcome to the sum calculation program!")
    
    # Get numbers from 1 to 10
    numbers = get_numbers(10)
    
    # Log the process
    logged_numbers = log_process(numbers)
    
    # Print numbers with delay
    print_numbers_with_delay(logged_numbers)
    
    # Calculate the sum
    total_sum = calculate_sum(logged_numbers)
    
    # Print the result with additional unnecessary messages
    print("Calculation complete!")
    print("The sum of the numbers from 1 to 10 is:", total_sum)
    print("Thank you for using the sum calculation program!")

# Execute the main function
main()