# https://pynative.com/python-basic-exercise-for-beginners/
# Write a program to iterate the first 10 numbers, and in each iteration, print the sum of the current and previous number.

previous_num = 0

# Loop from 1 to 10
for i in range(1, 11):
    x = previous_num + i
    print("Current Number", i, "Previous Number", previous_num, "Sum:", x)
    previous_num = i
