## What it does

The Python script takes a list of numbers as input from the user, sorts them using the bubble sort algorithm, and then prints the sorted list. Bubble sort is a simple sorting algorithm that repeatedly steps through the list, compares adjacent elements, and swaps them if they are in the wrong order. The script continues to prompt the user for input until the user decides to stop

## How we built it

The script is built using Python, a popular high-level programming language known for its readability and simplicity. The script is divided into three main functions: get_user_input, bubble_sort, and main. The get_user_input function prompts the user to enter the size of the list and then each number in the list. The bubble_sort function implements the bubble sort algorithm, which repeatedly goes through the list, compares adjacent elements, and swaps them if they are in the wrong order. The main function orchestrates the process by calling the get_user_input and bubble_sort functions and then printing the sorted list

## Challenges we ran into

The main challenge was to implement the bubble sort algorithm efficiently. Bubble sort has a worst-case and average time complexity of O(n^2), where n is the number of items being sorted. This makes it inefficient for large lists. To overcome this, we introduced an optimization in the bubble sort function to stop the algorithm if the list is already sorted

## Accomplishments that we're proud of

We're also proud of the optimization we introduced in the bubble sort function, which can significantly reduce the time complexity in the best-case scenario (i.e., when the list is already sorted)

## What we learned

We learned how to implement the bubble sort algorithm in Python and how to optimize it. We also learned how to interact with the user to get input and how to validate this input to ensure it's correct. Furthermore, we learned about the time complexity of the bubble sort algorithm and how it can be improved in certain scenarios

## What's next for Bubble Sort with Python

We could also improve the user interface, for example, by creating a graphical user interface (GUI) or a web application. Additionally, we could add more features, such as the ability to sort lists of strings or the ability to choose between ascending and descending order
