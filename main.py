nums = []

while True:
    name = input("Enter a number : ")
    nums.append(name)

    choice = input("Enter another number? (y / n)")
    if choice.casefold() == 'n':
        break


def sort(nums):
    for i in range(len(nums) - 1, 0, -1):
        for j in range(i):
            if nums[j] > nums[j + 1]:
                temp = nums[j]
                nums[j] = nums[j + 1]
                nums[j + 1] = temp


sort(nums)

print(nums)
