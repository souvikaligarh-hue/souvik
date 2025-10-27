# Task 2: Write and Append Data to a File
# Problem Statement: Write a Python program that:
# Takes user input and writes it to a file named output.txt.
# Appends additional data to the same file.
# Reads and displays the final content of the file.

# Takes user input and writes it to a file named output.txt.
user_input = input("Enter some text to write to the file: ")
with open('output.txt', 'w') as file:
    file.write(user_input + '\n')
    # Appends additional data to the same file.
    file.write("This is some additional text.\n")
# Reads and displays the final content of the file.
with open('output.txt', 'r') as file:
    content = file.read()
    print("Final content of the file:")
    print(content)  
# End of the code

