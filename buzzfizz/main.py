
chosen_number = int(input("Select a number between 1 and 100: "))


for i in range(1, chosen_number + 1):
    if i % 3 == 0:
        print("fizz")
    if i % 5 == 0:
        print("buzz")
    if i % 3 == 0 and i % 5 == 0:
        print("fizzbuzz")
    else:
        print(i)