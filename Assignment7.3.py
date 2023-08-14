def check_ascending_order(numbers):
    for i in range(1, len(numbers)):
        if numbers[i] < numbers[i - 1]:
            return False
    return True

print("Welcome! Input a sequence of numbers, and I'll determine if it's sorted in ascending order.")
user_input = input("Please enter a sequence of numbers (comma-separated): ")
number_sequence = [int(x) for x in user_input.split(",")]

if check_ascending_order(number_sequence):
    print("The sequence is sorted in ascending order.")
else:
    print("The sequence is not sorted in ascending order.")
