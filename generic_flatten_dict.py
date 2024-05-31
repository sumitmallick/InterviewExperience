# input = {
#     'user': {
#         'name': 'N'
#     },
#     'contact': [1, {"some": "data"}]
# }

# output = {
#     'user.name': 'N',
#     'contact.0': 1,
#     'contact.1.some':'data'
# }

# input = {
#     'user': {
#         'name': 'N'
#     },
#     'contact': [1, {"students": [{"name": "a"}, {"name": "b", "mobile": [123, 456, 789]}]}]
# }

def flatten_dict_numbers(input_dict, parent_key='', sep='.', pos = 0):
    items = []
    for k, v in input_dict.items():
        new_key = parent_key + sep + k if parent_key else k
        if isinstance(v, dict):
            items.extend(flatten_dict_numbers(v, new_key, sep=sep).items())
        elif isinstance(v, list):
            for i, item in enumerate(v, start=pos):
                item_key = new_key + sep + str(i)
                if isinstance(item, dict):
                    items.extend(flatten_dict_numbers(item, item_key, sep=sep).items())
                else:
                    items.append((item_key, item))
        else:
            items.append((new_key, v))
    return dict(items)

print(flatten_dict_numbers(input_dict=input))
