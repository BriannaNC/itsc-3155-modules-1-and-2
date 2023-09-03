def get_int(input1):
    while True:
        try:
            user_input = int(input(input1))
            return user_input
        except ValueError:
            print("Invalid input. Please enter an int.")

sum=0
for i in range(5):
    user_input= get_int(f"Enter int #{i+1}: ")
    sum += user_input
print(sum)
