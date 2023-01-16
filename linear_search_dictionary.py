def linear_search_dictionary(my_dictionary, target_value):

    for key, value in my_dictionary.items():
        if value == target_value:
            print("Successful match", key)
            return key
    print("Target is not in dictionary")
    return None

# def linear_search_dictionary(my_dictionary, target_value):
#     for key in my_dictionary:
#         if my_dictionary[key] == target_value:
#             print("Successful", key)
#             return key
#         print("Fail")
#         return None


my_dictionary = {"red": 5, "blue": 3, "yellow": 12, "green": 7}
linear_search_dictionary(my_dictionary, 5)
linear_search_dictionary(my_dictionary, 3)
linear_search_dictionary(my_dictionary, 8)
