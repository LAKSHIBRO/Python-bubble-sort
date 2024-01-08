def bubble_sort(numbers):
    for i in range(len(numbers)):
        for j in range(len(numbers) - 1):
            if numbers[j] > numbers[j + 1]:
                numbers[j], numbers[j + 1] = numbers[j + 1], numbers[j]
    return numbers

def get_user_input():
    number_list = []
    n = int(input("Enter the list size: "))
    for i in range(n):
        item = int(input(f"Enter number at index {i}: "))
        number_list.append(item)
    return number_list

def main():
    numbers = get_user_input()
    sorted_numbers = bubble_sort(numbers)
    print("Sorted list is ", sorted_numbers)

if __name__ == "__main__":
    main()
