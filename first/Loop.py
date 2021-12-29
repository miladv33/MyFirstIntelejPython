numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]

for num in numbers:
    if num == 5:
        continue
    print(f'number is {num}')

for i in range(0, 2):
    print("*")

for num in numbers:
    if num == 5:
        break
    print(f'number is {num}')

for i in range(len(numbers)):
    print(numbers[i])

count = 0
while count < 10:
    print(f"count is {count}")
    count += 1
