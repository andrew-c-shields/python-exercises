# https://pynative.com/python-basic-exercise-for-beginners/
# Write a Python code to remove characters from a string from 0 to n and return a new string.
# For Example:
#   remove_chars("PYnative", 4) so output must be tive. Here, you need to remove the first four characters from a string.
#   remove_chars("PYnative", 2) so output must be native. Here, you need to remove the first two characters from a string.
# Note: n must be less than the length of the string.

def remove_chars(word, n):
    print('Original string:', word)
    x = word[n:]
    return x

print("Removing characters from a string")
print(remove_chars("pynative", 4))
print(remove_chars("pynative", 2))