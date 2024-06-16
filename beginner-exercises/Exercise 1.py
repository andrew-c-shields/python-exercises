# https://pynative.com/python-basic-exercise-for-beginners/
# Given two integer numbers, return their product only if they product is equal to or lower than 1000. Otherwise, return their sum.

def product_or_sum(num1, num2):
    product = num1 * num2
    
    if product <= 1000:
        return product
    else:
        return num1 + num2
        
result = product_or_sum(20, 30)
print("The result is", result)

result = product_or_sum(40, 30)
print("The result is", result)
