# FORMAT :
# basic
print("\nThis is a string {}".format("INSERTED")) 
# index
print("\nThe {2} {1} {0}".format("fox", "brown", "quick")) 
# keywords
print("\nThe {f} {b} {q}".format(f="fox", b="brown", q ="quick")) 
# number formatting
result = 100/777
print("\nThe result was {r:1.3f}".format(r=result))
    # 1 - width (white space)
    # 3 - precision - numbers past decimal point

# Formatted string literals (since python 3.6):

name = "Jose"
print(f'Hello, his name is {name}')
    # the f is mandatory
