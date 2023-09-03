def make_dict(input_str):
    input_str=input_str.lower()
    input_str=input_str.replace(" ", "")
    dict_result={}
    for i in input_str:
        dict_result[i]= input_str.count(i)
        if dict_result[i] in dict_result:
            dict_result[i]
    return dict_result

user_input=str(input("Enter a string: "))
print(make_dict(user_input))