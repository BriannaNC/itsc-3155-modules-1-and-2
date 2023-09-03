def get_unique_list(input_list):
    unique_list=[]
    for num in input_list:
        if num not in unique_list:
            unique_list.append(num)
    return unique_list  

user_list=[1,4,5,1,3,5]
print(get_unique_list(user_list))

      