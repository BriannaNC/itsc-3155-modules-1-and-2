def shift_lower_front(input1):
    lower=""
    upper=""

    input1= input1.replace(" ", "")

    for i in input1:
        if i.islower():
            lower+=i
        else:
            upper+=i
    output= lower+upper
    return output
user_input= str(input("Enter a string: "))    
user_output= shift_lower_front(user_input)
print(user_output)