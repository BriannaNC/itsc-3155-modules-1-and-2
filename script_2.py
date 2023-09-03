def get_combined_dict(input_dict1,input_dict2):
    combined_dict={}
    for key in input_dict1:
        if key in input_dict2:
            combined_dict[key]= input_dict1.get(key) + input_dict2.get(key)
    return combined_dict

dict1={'a':5,'b':12,'c':3,'d':9}
dict2={'b':4,'c':9,'d':10,'e':16}

print(get_combined_dict(dict1,dict2))
    