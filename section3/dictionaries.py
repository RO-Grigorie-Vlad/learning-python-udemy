#definition
my_dict = {"key1": "value1", "key2": "value2"}
prices_lookup = {"apple": 1.30, "bananas": 1.5}
prices_lookup2 = {1: 1.30, "bananas": 1.5}
    #keys don't have to be strings - but they usually are
    #keys HAVE to be unique
    #dicts dont keep order, unlike lists

#dicts can be nested (any type is good for the value)
nested_dict = {"key1": 2, "key2": {"location1" : 4}}

#get value at key
print(my_dict.get("key1"))
print(my_dict.get("key2"))
print(my_dict["key2"])
print(prices_lookup.get("apple"))
print(prices_lookup.get("bananas"))
print(nested_dict["key2"]["location1"])

#add/change value of key
my_dict["k3"] = "value3"
print(my_dict["k3"])

#get all keys, values, items
print(my_dict.keys())
print(my_dict.values())
print(my_dict.items())