def sort_numbers(numbers):
    def find_and_remove_smallest(numbers):
        smallest = numbers[0]
        index = 0
        for i in range(len(numbers)):
            if numbers[i] < smallest:
                smallest = numbers[i]
                index = i
        new_numbers = []
        for i in range(len(numbers)):
            if i != index:
                new_numbers.append(numbers[i])
        return smallest, new_numbers

    sorted_list = []
    while len(numbers) > 0:
        smallest, numbers = find_and_remove_smallest(numbers)
        sorted_list.append(smallest)
    return sorted_list

numbers = [5, 2, 9, 1, 5, 6]
sorted_numbers = sort_numbers(numbers)
print("Sorted numbers:", sorted_numbers)